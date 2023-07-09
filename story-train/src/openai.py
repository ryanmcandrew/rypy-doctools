import openai
from utilities import ApplicationLogFormatter

class OpenaiClient:
    def __init__(self):
        logger = ApplicationLogFormatter()
        self.logger = logger.buildLogger(__name__ + '.' + self.__class__.__name__)

    def create_storyboard(self, settings):
        pass

    def define_character(self, character):
        pass

    def define_plot(self, plot):
        pass

    def define_environment(self, environment):
        pass

    def __create_storyboard_unit_image(self):
        pass

    def __create_storyboard_unit_dialogue(self):
        pass

