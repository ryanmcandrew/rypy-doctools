import json
import logging
import openai
import typing
import os
import requests
import random

openai.organization = ""
openai.api_key = os.environ.get('OPENAI_API_KEY')

GPT_3_5_TURBO_PRICE_EQUATION = lambda x: (x/1000) * 0.002
TARGET_CHARACTERS_PER_SUBJECT = 600

environment = {
    'outputFilePath': 'output',
    'outputFileBaseName': 'book',
    'configFilePath': 'src/instructions.json',
    'openai_model': 'gpt-3.5-turbo',
    'md_output_top_level_folder': 'out/',
    'static_content_dir': 'src/static',
    'download_dir': './downloads',
    'image_result_filepaths':[]
}

def load_images():
    file_dir_path = environment['download_dir']
    
    files = os.scandir(file_dir_path)

    sorted_files = sorted(files, key=lambda item: item.stat().st_mtime)

    for file in sorted_files:
        environment['image_result_filepaths'].append(file.path)

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
    

class OpenAiClient:
    def __init__(self):
        logger = ApplicationLogFormatter()
        self.logger = logger.buildLogger(__name__ + '.' + self.__class__.__name__)

    def send_text_to_openai(self, text:typing.List[str]) -> typing.List[str]:
        '''
            load the book config, form it into a complete instruction for openai api, then send it and return the results
        '''

        results = []
        urls = []
                        
        self.logger.info('starting chatgpt api request for:' + str(text))
        
        result = openai.Image.create(
            prompt=text,
            n=1,
            # size="1024x1024"
            # size="512x512"
            size="256x256"
        )

        if result is not None:

            for res in result.data:
                response = requests.get(res.url)
                image_content = response.content
                if not os.path.exists(environment['download_dir']):
                    os.makedirs(environment['download_dir'])
                filePath = environment['download_dir'] + '/image_' + str(result.created) + "_" + str(random.randint(1,100)) + '.jpg'
                
                with open(filePath, 'wb') as f:
                    f.write(image_content)
                    print("Successfully wrote " + filePath + " to disk")
                
                results.append(filePath)
                environment['image_result_filepaths'].append(filePath)
        else:
            self.logger.info('failed to receive data from openai')    

        self.logger.info('finished openai api requests')

        return results
