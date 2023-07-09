import json
import logging

def load_images():
    pass

def load_characters():
    pass

def load_environment():
    pass

def load_event():
    pass

def load_dialogue():
    pass

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