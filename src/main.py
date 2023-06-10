from utilities import ApplicationLogFormatter, InputHandler, OutputHandler, OpenAiClient, calculate_cost_of_configuration

def main():
    '''
    
        flow:
            - load the configuration
                - import json.load(path)
            - construct list of messages to send
            - for each constructed, send instructions to chatgpt
                - export the chat result in a file

    '''
    logger = ApplicationLogFormatter(__name__)
    logger = logger.buildLogger()

    input_handler = InputHandler()
    output_handler = OutputHandler()
    gpt_client = OpenAiClient()
    
    book_config = input_handler.load_books_config()

    messages = input_handler.load_messages_from_books(book_config)
    num_tokens, calc = calculate_cost_of_configuration(messages)
    logger.warning("Estimated sending and receiving " + str(num_tokens) + " total tokens which will cost $" + str(calc))
    
    progress = input("Continue? (Y/n): ")
    if progress == "Y" or progress == "y" or progress == '':
        result = gpt_client.send_to_chatgpt(book_config, input_handler.get_number_of_subjects(book_config) -1 )
        # result = gpt_client.send_to_chatgpt(book_config, 1 )
        output_handler.write_output_to_md(result)


if __name__ == '__main__':
    main()