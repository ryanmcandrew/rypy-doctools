import unittest

from src.main import load_books_config, load_messages_from_books, calculate_cost_of_configuration
from src.utilities import ApplicationLogFormatter
import logging

class TestModel(unittest.TestCase):
    
    def setUp(self):
        self.logger = ApplicationLogFormatter()
        self.logger = self.logger.buildLogger()


    def test_calculation(self):
        messages = load_messages_from_books(load_books_config())
        num_tokens, calc = calculate_cost_of_configuration(messages)
        self.logger.info(num_tokens)
        self.logger.info(calc)

    def test_config_load(self):
        messages = load_messages_from_books(load_books_config())
        for i in messages:
            self.logger.info(str(i))