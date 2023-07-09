from PyQt5.QtWidgets import QApplication, QMainWindow

# from ui.model import Model
# from ui.view import View
# from ui.controller import Controller

from ui.model import ToolbarModel, CharacterUnitModel
from ui.view import MainWindowView, ToolbarView, CharacterUnitView
from ui.controller import MainWindowController, ToolbarViewController, CharacterUnitViewController

import sys

class GuiBuilder:
    def build_home_screen(self):
        pass

    def build_character_menu(self):
        pass

    def build_environment_menu(self):
        pass

    def build_event_menu(self):
        pass

    def build_dialogue_menu(self):
        pass

    def build_settings_menu(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # model = Model()
    # view = View()
    # controller = Controller(model, view)
    # toolbar_model = ToolbarModel()
    # toolbar_view = ToolbarView()
    # toolbar_controller = ToolbarViewController(toolbar_model, toolbar_view)
    # toolbar_view.show()

    # character_model = CharacterUnitModel()
    # character_view = CharacterUnitView()
    # character_controller = CharacterUnitViewController(character_model, character_view)
    # character_view.show()

    # print(app.receivers)
    # app.
    main_window_view = MainWindowView()
    # main_window_controller = MainWindowController(toolbar_model, main_window_view.toolbar)

    main_window_view.show()
    # view.show()

    sys.exit(app.exec_())