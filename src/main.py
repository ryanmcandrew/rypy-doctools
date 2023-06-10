import openai
import json
import typing
import os
import datetime
from mdutils import MdUtils

from model import Book, Chapter, GptResultType
from utilities import ApplicationLogFormatter, environment


openai.organization = ""
openai.api_key = os.environ.get('OPENAI_API_KEY')

logger = ApplicationLogFormatter()
logger = logger.buildLogger()

GPT_3_5_TURBO_PRICE_EQUATION = lambda x: (x/1000) * 0.002
TARGET_CHARACTERS_PER_SUBJECT = 600

def load_books_config() -> typing.List[Book]:
    '''
        loads the config json into settings.messages
    '''
    with open(environment['configFilePath']) as data:
        
        configFile = json.load(data)
        book = None
        books_prompts = []

        for cfg_book in configFile['books']:
            book = Book()
            book.name = cfg_book['name']
            for cfg_chapter in cfg_book['chapters']:
                chapter = Chapter()
                chapter.name = cfg_chapter['name']
                chapter.target_characters_per_subject = cfg_chapter['target_characters_per_subject']
                chapter.helper_prompt_head = cfg_chapter['helper_prompt_head']
                chapter.helper_prompt_tail = cfg_chapter['helper_prompt_tail']
                chapter.subjects = cfg_chapter['subjects']
                book.append_chapter(chapter)
            books_prompts.append(book)

        return books_prompts
    
def get_number_of_subjects(books: typing.List[Book]):
    count = 0

    for book in books:
        for chapter in book.chapters:
            for subject in chapter.subjects:
                count += 1

    return count
    
def load_messages_from_books(books: typing.List[Book]):

    messages = []

    for book in books:
        for chapter in book.chapters:
            for subject in chapter.subjects:
                messages.append(chapter.helper_prompt_head + " " + subject + " " + chapter.helper_prompt_tail)

    return messages

def calculate_cost_of_configuration(data):
    '''
        https://openai.com/pricing

        parameter: data : typing.List[str]
            will come in the form of a list of questions to send GPT, such as:
            [
                "Write me a story about x",
                "write me a simile about x",
                "etc"
            ]
    '''
    
    count = 0

    for i in data:
        #count the length of the question string at each array index
        count += len(i)

    #use the target characters for each response from chatgpt and multiply by the number of questions
    count += TARGET_CHARACTERS_PER_SUBJECT * len(data)

    return (count, GPT_3_5_TURBO_PRICE_EQUATION(count))


def send_to_chatgpt(books:typing.List[Book], subject_stop_index = 0) -> GptResultType:
    '''
        load the book config, form it into a complete instruction for openai api, then send it and return the results
    '''

    global logger


    results = []

    iter = 0
    for book in books:
        for chapter in book.chapters:
            
            for subject in chapter.subjects:
                if iter <= subject_stop_index:
                    a_result = GptResultType()
                    a_result.subject = subject
                    a_result.book = book.name
                    a_result.chapter = chapter.name
                    a_result.question = chapter.helper_prompt_head + " " + a_result.subject + " " + chapter.helper_prompt_tail
                    
                    logger.info('starting chatgpt api request for:' + str(book.name) + " - Chapter: " + str(chapter.name).title() + " - Subject: " + str(subject))
                    completion = openai.ChatCompletion.create(
                        model=environment['openai_model'],
                        messages=[
                            {
                                "role": "user", 
                                "content": a_result.question
                            }
                        ]
                    )
                    logger.info('finished chatgpt api request')
                    
                    a_result.answer = completion.choices[0].message['content']
                    results.append(a_result)
                    iter += 1
                else:
                    break

    return results

def write_output_to_md(results:typing.List[GptResultType]):

    '''
        Print the results of send_to_chatgpt to md files
    '''

    global logger

    mainReadMe = MdUtils(file_name='readme.md', title='Master Readme File', author='Ryan McAndrew bot')
    mainReadMe.write('# Table of Contents\n\n')
    for result in results:
        logger.info('starting to write to .md')
        
        book_str = result.book.title().replace(" ", "")
        chapter_str = result.chapter.title().replace(" ", "")
        subject_str = result.subject.title().replace(" ", "")

        directory_path = environment['md_output_top_level_folder'] + book_str + '/' + chapter_str + '/'

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        full_file_path = directory_path + subject_str + "_" + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M") + '.md'
        
        mainReadMe.write('- ')
        mainReadMe.write(f"[{result.book.title()}/{result.subject.title()}]({full_file_path})")
        mainReadMe.write('\n')

        mdFile = MdUtils(file_name=full_file_path, title=result.subject, author='Ryan McAndrew bot')
        mdFile.write(result.answer)
        mdFile.create_md_file()
        logger.info('completed writing subject to:' + full_file_path)

    mainReadMe.create_md_file()
    logger.info('completed main readme')

def main():
    '''
    
        flow:
            - load the configuration
                - import json.load(path)
            - construct list of messages to send
            - for each, send instructions to chatgpt
                - export the chat result in a file
                - cache result

    '''
    global logger
    
    book_config = load_books_config()

    messages = load_messages_from_books(book_config)
    num_tokens, calc = calculate_cost_of_configuration(messages)
    logger.warning("Estimated sending and receiving " + str(num_tokens) + " total tokens which will cost $" + str(calc))
    
    progress = input("Continue? (Y/n): ")
    if progress == "Y" or progress == "y" or progress == '':
        result = send_to_chatgpt(book_config, get_number_of_subjects(book_config) -1 )
        write_output_to_md(result)


if __name__ == '__main__':
    main()
