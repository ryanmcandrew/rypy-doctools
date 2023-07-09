from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QAction, QToolBar

from model import SettingsModel, MainModel
from view import MainView, SettingsView
from controller import MainViewController, SettingsViewController

from utilities import ApplicationLogFormatter
from utilities import load_images

import sys

class MainWindowView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings_model = SettingsModel()
        self.settings_view = SettingsView()
        self.settings_controller = SettingsViewController(self.settings_model, self.settings_view)

        self.main_model = MainModel()
        self.main_view = MainView()
        self.main_controller = MainViewController(self.main_model, self.main_view)

        self.setWindowTitle("PyQt5 Gpt Images")

        toolbar = self.addToolBar('Toolbar e')
        editToolbar = QToolBar()
        toolbar.setOrientation(1)

        home_action = QAction('Home', self)
        settings_action = QAction('Settings', self)

        home_action.triggered.connect(self.show_homescreen)
        settings_action.triggered.connect(self.show_settings)

        editToolbar.addAction(home_action)
        editToolbar.addAction(settings_action)
        toolbar.addWidget(editToolbar)

        self.stack = QStackedWidget()

        self.stack.addWidget(self.main_view)
        self.stack.addWidget(self.settings_view)

        self.setCentralWidget(self.stack)


    def show_homescreen(self):
        self.stack.setCurrentIndex(0)

    def show_settings(self):
        self.stack.setCurrentIndex(1)

if __name__ == '__main__':

    logger = ApplicationLogFormatter()
    logger = logger.buildLogger(__name__ + '.')

    logger.info('application started')

    load_images()
    
    app = QApplication(sys.argv)
    main_window_view = MainWindowView()

    logger.info('showing main window')
    main_window_view.show()
    sys.exit(app.exec_())