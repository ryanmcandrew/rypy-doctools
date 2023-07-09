import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QLineEdit, QPushButton, QPlainTextEdit,QSlider
from PyQt5.QtWidgets import QLabel, QToolBar
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QPixmap

import utilities

class MainView(QWidget):
    def __init__(self):
        super().__init__()

        logger = utilities.ApplicationLogFormatter()
        self.logger = logger.buildLogger(__name__ + '.' + self.__class__.__name__)

        if len(utilities.environment['image_result_filepaths']) > 0:
            file_path = utilities.environment['image_result_filepaths'][-1]
        else:
            file_path = 'src/static/question.jpg'

        self.pix = QPixmap(file_path)
        self.image_area = QLabel()
        self.image_area.setPixmap(self.pix)
        self.image_description_label = QLabel("Image description")
        self.image_description = QLineEdit()
        self.send_button = QPushButton("Send")

        # self.slider = QSlider(self)
        # self.slider.setGeometry(50, 200, 300, 20)
        # self.slider.valueChanged.connect(self.update_slider)

        self.unit_layout = QVBoxLayout()
        # self.unit_layout.addWidget(self.slider)
        self.unit_layout.addWidget(self.image_area)
        self.unit_layout.addWidget(self.image_description_label)
        self.unit_layout.addWidget(self.image_description)
        self.unit_layout.addWidget(self.send_button)

        self.setLayout(self.unit_layout)
    
    # def update_slider(self):
    #     index = self.slider.value()
    #     self.logger.info(index)
        # self.pix

    def update_image_area(self):
        self.unit_layout.removeWidget(self.image_area)
        self.unit_layout.removeWidget(self.image_description_label)
        self.unit_layout.removeWidget(self.image_description)
        self.unit_layout.removeWidget(self.send_button)
        self.pix = QPixmap(utilities.environment['image_result_filepaths'][-1])
        self.image_area.setPixmap(self.pix)
        self.unit_layout.addWidget(self.image_area)
        self.unit_layout.addWidget(self.image_description_label)
        self.unit_layout.addWidget(self.image_description)
        self.unit_layout.addWidget(self.send_button)

class SettingsView(QWidget):
    def __init__(self):
        super().__init__()


        self.api_key_label = QLabel("Openai API key")
        self.api_key = QLineEdit()

        self.data_dir_label = QLabel("Path to data store")
        self.data_dir = QLineEdit()

        self.update_button = QPushButton("Update")
        self.export_button = QPushButton("Export Image")

        layout = QVBoxLayout()
        # layout.addWidget(self.name_input_box)
        # layout.addWidget(self.trait_input_box)
        layout.addWidget(self.api_key_label)
        layout.addWidget(self.api_key)
        layout.addWidget(self.data_dir_label)
        layout.addWidget(self.data_dir)
        layout.addWidget(self.update_button)
        layout.addWidget(self.export_button)

        self.setLayout(layout)

# -----------------------------------------------------------------
# -----------------------------------------------------------------
# Helper Widgets
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# class SliderView(QWidget):
