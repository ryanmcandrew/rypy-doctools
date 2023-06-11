import logging
import typing
import json
from mdutils import MdUtils
import openai
import os
import datetime

from model import Book, Chapter, GptResultType

openai.organization = ""
openai.api_key = os.environ.get('OPENAI_API_KEY')

GPT_3_5_TURBO_PRICE_EQUATION = lambda x: (x/1000) * 0.002
TARGET_CHARACTERS_PER_SUBJECT = 600

environment = {
    'outputFilePath': 'output',
    'outputFileBaseName': 'book',
    'configFilePath': 'src/instructions.json',
    'openai_model': 'gpt-3.5-turbo',
    'md_output_top_level_folder': 'out/'
}

# ------------------------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------------------------

class ApplicationLogFormatter(logging.Formatter):

    GREEN = '\u001b[32m'
    BLUE = '\u001b[34m'
    YELLOW = '\u001b[33m'
    RED = '\u001b[31m'
    RESET = '\u001b[0m'
    WHITE = '\u001b[37;1m'
    format_string = '[ %(levelname)s ] %(message)s'


    def __init__(self, fmt=None, datefmt=None, style='%'):
        super(ApplicationLogFormatter, self).__init__(fmt=self.format_string, datefmt=datefmt, style=style)

    def format(self, record):
        '''
        '''

        record.msg = f"{self.BLUE}[ {self.name}  ] : {self.WHITE}{record.msg} "
        record.levelname
        if record.levelno == logging.DEBUG:
            record.levelname = f"{self.GREEN}DEBUG{self.WHITE}"
        elif record.levelno == logging.INFO:
            record.levelname = f"{self.GREEN}INFO{self.WHITE}"
        elif record.levelno == logging.WARNING:
            record.levelname = f"{self.YELLOW}WARNING{self.WHITE}"
        elif record.levelno == logging.ERROR:
            record.levelname = f"{self.YELLOW}ERROR{self.WHITE}"
        elif record.levelno == logging.CRITICAL:
            record.levelname = f"{self.RED}CRITICAL{self.WHITE}"
        elif record.levelno == logging.FATAL:
            record.levelname = f"{self.RED}FATAL{self.WHITE}"

        return super(ApplicationLogFormatter, self).format(record)
    
    def buildLogger(self, name = 'default'):
        '''
        '''

        self.name = name

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self)
        
        log = logging.Logger(level=logging.DEBUG, name=self.name)
        log.setLevel('DEBUG')
        log.addHandler(console_handler)

        return log

class InputHandler:
    def __init__(self):
        logger = ApplicationLogFormatter()
        self.logger = logger.buildLogger(__name__ + '.' + self.__class__.__name__)


    def load_books_config(self) -> typing.List[Book]:
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
        
    def get_number_of_subjects(self, books: typing.List[Book]) -> int:
        '''
        '''

        count = 0

        for book in books:
            for chapter in book.chapters:
                for subject in chapter.subjects:
                    count += 1

        return count
        
    def load_messages_from_books(self, books: typing.List[Book]) -> typing.List[str]:
        '''
        '''

        messages = []

        for book in books:
            for chapter in book.chapters:
                for subject in chapter.subjects:
                    messages.append(chapter.helper_prompt_head + " " + subject + " " + chapter.helper_prompt_tail)

        return messages

class OutputHandler:
    def __init__(self):
        '''
        '''

        logger = ApplicationLogFormatter()
        self.logger = logger.buildLogger(__name__ + '.' + self.__class__.__name__)

    def write_chat_result(self, result:GptResultType) -> None:
        '''
        '''

        self.logger.info('starting to write to gpt generated .md')
        
        book_str = result.book.title().replace(" ", "")
        chapter_str = result.chapter.title().replace(" ", "")
        subject_str = result.subject.title().replace(" ", "")

        directory_path = environment['md_output_top_level_folder'] + book_str + '/' + chapter_str + '/'

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        full_file_path = directory_path + subject_str + "_" + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M") + '.md'

        mdFile = MdUtils(file_name=full_file_path, title=result.subject, author='Ryan McAndrew bot')
        mdFile.write(result.answer)
        mdFile.create_md_file()
        self.logger.info('completed writing subject to:' + full_file_path)

    def write_main_readme(self, results:typing.List[GptResultType]) -> None:
        '''
        '''

        current_chapter = None
        current_book = None
        mainReadMe = MdUtils(file_name='readme.md', title='Master Readme File', author='Ryan McAndrew bot')
        mainReadMe.write('# Table of Contents\n\n')

        for result in results:
            
            if result.book != current_book:
                current_book = result.book
                mainReadMe.write( f'## {current_book.title()} \n--------------------\n' )

            if result.chapter != current_chapter:
                current_chapter = result.chapter
                mainReadMe.write( f'### {current_chapter.title()}\n\n')


            self.logger.info('starting to write to gpt generated .md')
            
            book_str = result.book.title().replace(" ", "")
            chapter_str = result.chapter.title().replace(" ", "")
            subject_str = result.subject.title().replace(" ", "")

            directory_path = environment['md_output_top_level_folder'] + book_str + '/' + chapter_str + '/'


            full_file_path = directory_path + subject_str + "_" + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M") + '.md'
            
            mainReadMe.write(f"-  [{result.subject.title()}]({full_file_path})\n")      

            self.logger.info('completed writing subject to:' + full_file_path)

        mainReadMe.create_md_file()
        self.logger.info('completed main readme')

        current_chapter = None
        current_book = None

    def write_output_to_md(self, results:typing.List[GptResultType]):

        '''
            Print the results of send_to_chatgpt to md files
        '''

        current_chapter = None
        current_book = None
        mainReadMe = MdUtils(file_name='readme.md', title='Master Readme File', author='Ryan McAndrew bot')
        mainReadMe.write('# Table of Contents\n\n')

        for result in results:
            
            if result.book != current_book:
                current_book = result.book
                mainReadMe.write( f'## {current_book.title()} \n--------------------\n' )

            if result.chapter != current_chapter:
                current_chapter = result.chapter
                mainReadMe.write( f'### {current_chapter.title()}\n\n')


            self.logger.info('starting to write to gpt generated .md')
            
            book_str = result.book.title().replace(" ", "")
            chapter_str = result.chapter.title().replace(" ", "")
            subject_str = result.subject.title().replace(" ", "")

            directory_path = environment['md_output_top_level_folder'] + book_str + '/' + chapter_str + '/'

            if not os.path.exists(directory_path):
                os.makedirs(directory_path)

            full_file_path = directory_path + subject_str + "_" + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M") + '.md'
            
            mainReadMe.write(f"-  [{result.subject.title()}]({full_file_path})\n")      

            mdFile = MdUtils(file_name=full_file_path, title=result.subject, author='Ryan McAndrew bot')
            mdFile.write(result.answer)
            mdFile.create_md_file()
            self.logger.info('completed writing subject to:' + full_file_path)

        mainReadMe.create_md_file()
        self.logger.info('completed main readme')

class OpenAiClient:
    def __init__(self):
        logger = ApplicationLogFormatter()
        self.logger = logger.buildLogger(__name__ + '.' + self.__class__.__name__)

    def send_to_chatgpt(self, books:typing.List[Book], subject_stop_index = 0) -> GptResultType:
        '''
            load the book config, form it into a complete instruction for openai api, then send it and return the results
        '''

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
                        
                        self.logger.info('starting chatgpt api request for:' + str(book.name) + " - Chapter: " + str(chapter.name).title() + " - Subject: " + str(subject))
                        completion = openai.ChatCompletion.create(
                            model=environment['openai_model'],
                            messages=[
                                {
                                    "role": "user", 
                                    "content": a_result.question
                                }
                            ]
                        )
                        self.logger.info('finished chatgpt api request')
                        
                        a_result.answer = completion.choices[0].message['content']
                        results.append(a_result)
                        iter += 1
                    else:
                        break

        return results

# ------------------------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------------------------

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