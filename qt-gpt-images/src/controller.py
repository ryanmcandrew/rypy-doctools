import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QPlainTextEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot

import model as model
import view as view
from utilities import OpenAiClient, ApplicationLogFormatter

class SettingsViewController(QWidget):
    def __init__(self, tmodel: typing.Optional[model.SettingsModel] = None, tview: typing.Optional[view.SettingsView] = None):
        super().__init__()

        self.model = tmodel
        self.view = tview

        self.view.update_button.clicked.connect(self.handle_update_button)
        self.view.export_button.clicked.connect(self.handle_export_button)


    def handle_openai_api_key(self):
        pass

    def handle_data_dir(self):
        pass

    def handle_update_button(self):
        pass

    def handle_export_button(self):
        pass

class EditImageView(QWidget):
    def __init__(self):
        pass

    def handle_handle_image_selector(self):
        pass

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

class MainViewController(QWidget):
    def  __init__(self, tmodel: typing.Optional[model.MainModel] = None, tview: typing.Optional[view.MainView] = None, settings: typing.Optional[model.SettingsModel] = None):
        super().__init__()

        logger = ApplicationLogFormatter()
        self.logger = logger.buildLogger(__name__ + '.' + self.__class__.__name__)

        self.model = tmodel
        self.view = tview

        self.view.image_description.textChanged.connect(self.handle_description)
        self.view.send_button.clicked.connect(self.handle_send_button)

    def handle_description(self):
        self.model.description = self.view.image_description.text()

    def handle_send_button(self):
        client = OpenAiClient()
        client.send_text_to_openai(self.model.description)
        self.view.update_image_area()


# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------



