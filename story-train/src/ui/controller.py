import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QPlainTextEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot

import ui.model as model
import ui.view as view

# class Controller:
#     def __init__(self, model: typing.Optional[model.Model] = None, view: typing.Optional[view.View] = None):
#         self.model = model
#         self.view = view

#         self.view.submit_button.clicked.connect(self.handle_submit)

#     def handle_submit(self):
#         text = self.view.input_box.text()
#         self.model.set_text(text)
#         print("Submitted text:", text)

class ToolbarEmitter(QObject):
    signal = pyqtSignal(str, name='test nb')

class ToolbarViewController(QWidget):
    def __init__(self, tmodel: typing.Optional[model.ToolbarModel] = None, tview: typing.Optional[view.ToolbarView] = None):
        super().__init__()

        self.signal = pyqtSignal(name='cool')
        self.model = tmodel
        self.view = tview

        self.signal = ToolbarEmitter()
        self.signal.signal.connect(self.test)

        # self.messages_bus = QMessageBus()
        self.view.home_button.clicked.connect(self.handle_home_button)
        self.view.characters_button.clicked.connect(self.handle_characters_button)
        self.view.environment_button.clicked.connect(self.handle_environment_button)
        self.view.event_button.clicked.connect(self.handle_event_button)
        self.view.dialogue_button.clicked.connect(self.handle_dialogue_button)
        self.view.settings_button.clicked.connect(self.handle_settings_button)
        # self.view.home_button.

    def test(self, value):
        print(value)

    def handle_home_button(self):
        # print('homeclicked')
        self.signal.signal.emit('emitted test')


    def handle_characters_button(self):
        pass

    def handle_environment_button(self):
        pass

    def handle_event_button(self):
        pass

    def handle_dialogue_button(self):
        pass

    def handle_settings_button(self):
        pass

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

class CharacterUnitViewController(QWidget):
    def __init__(self, tmodel: typing.Optional[model.CharacterUnitModel] = None, tview: typing.Optional[view.CharacterUnitView] = None):
        super().__init__()

        self.model = tmodel
        self.view = tview

        self.view.uid_control.returnPressed.connect(self.handle_uid_control)
        self.view.name_control.returnPressed.connect(self.handle_name_control)
        self.view.species_control.returnPressed.connect(self.handle_species_control)
        self.view.traits_control.returnPressed.connect(self.handle_traits_control)
        self.view.abilities_control.returnPressed.connect(self.handle_abilities_control)
        self.view.aspirations_control.returnPressed.connect(self.handle_aspirations_control)
        self.view.development_control.returnPressed.connect(self.handle_development_control)
        self.view.occupation_control.returnPressed.connect(self.handle_occupation_control)
        self.view.interests_control.returnPressed.connect(self.handle_interests_control)
        self.view.habits_control.returnPressed.connect(self.handle_habits_control)
        self.view.outfit_control.returnPressed.connect(self.handle_outfit_control)
        self.view.face_control.returnPressed.connect(self.handle_face_control)
        self.view.body_type_control.returnPressed.connect(self.handle_body_type_control)
        self.view.background_control.returnPressed.connect(self.handle_background_control)
        self.view.relationships_control.returnPressed.connect(self.handle_relationships_control)
        self.view.age_control.returnPressed.connect(self.handle_age_control)
        self.view.beliefs_control.returnPressed.connect(self.handle_beliefs_control)
        self.view.home_type_control.returnPressed.connect(self.handle_home_type_control)
        self.view.is_hero_control.returnPressed.connect(self.handle_is_hero_control)
        self.view.is_villain_control.returnPressed.connect(self.handle_is_villain_control)

    def handle_uid_control(self):
        pass

    def handle_name_control(self):
        pass

    def handle_species_control(self):
        pass

    def handle_traits_control(self):
        pass

    def handle_abilities_control(self):
        pass

    def handle_aspirations_control(self):
        pass

    def handle_development_control(self):
        pass

    def handle_occupation_control(self):
        pass

    def handle_interests_control(self):
        pass

    def handle_habits_control(self):
        pass

    def handle_outfit_control(self):
        pass

    def handle_face_control(self):
        pass

    def handle_body_type_control(self):
        pass

    def handle_background_control(self):
        pass

    def handle_relationships_control(self):
        pass

    def handle_age_control(self):
        pass

    def handle_beliefs_control(self):
        pass

    def handle_home_type_control(self):
        pass

    def handle_is_hero_control(self):
        pass

    def handle_is_villain_control(self):
        pass

class EnvironmentUnitViewController(QWidget):
    def __init__(self):
        super().__init__()

class EventUnitViewController(QWidget):
    def __init__(self):
        super.__init__()

        # self.trait_input_boxes = []

        # self.event_input_box = QLineEdit()
        # self.topic_input_box = QLineEdit()

        # self.add_new_trait_button = QPushButton("Add New Trait")

        # layout = QVBoxLayout()
        # layout.addWidget(self.name_input_box)
        # layout.addWidget(self.trait_input_box)
        # layout.addWidget(self.add_new_trait_button)

class DialogueUnitViewController(QWidget):
    def __init__(self):
        super().__init__()

class StoryBoardUnitViewController(QWidget):
    def __init__(self):
        super().__init__()

        # self.image = None
        # self.description = QPlainTextEdit(self)
        # self.dialogue = QPlainTextEdit(self)

        # self.unit_layout = QVBoxLayout()
        # self.unit_layout.addWidget(self.description)
        # self.unit_layout.addWidget(self.dialogue)

        # self.setLayout(self.unit_layout)

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

class CharacterContainerViewController(QWidget):
    def __init__(self):
        super().__init__()

        # self.character_units = []
        # self.character_units.append(EventUnitView())

        # self.unit_layout = QVBoxLayout()
        # self.unit_layout.addWidget(self.character_units[0])

class EnvironmentContainerViewController(QWidget):
    def __init__(self):
        super().__init__()

        # self.environment_units = []
        # self.environment_units.append(EventUnitView())

        # self.unit_layout = QVBoxLayout()
        # self.unit_layout.addWidget(self.environment_units[0])

class EventContainerViewController(QWidget):
    def __init__(self):
        super().__init__()

        # self.event_units = []
        # self.event_units.append(EventUnitView())

        # self.unit_layout = QVBoxLayout()
        # self.unit_layout.addWidget(self.event_units[0])

class DialogueContainerViewController(QWidget):
    def __init__(self):
        super().__init__()

        # self.dialogue_units = []
        # self.dialogue_units.append(DialogueUnitView())

        # self.unit_layout = QVBoxLayout()
        # self.unit_layout.addWidget(self.dialogue_units[0])

class StoryBoardContainerViewController(QWidget):
    def __init__(self):
        super().__init__()

        # self.storyboard_units = []

        # self.storyboard_units.append(StoryBoardUnitView())

        # self.unit_layout = QVBoxLayout()
        # self.unit_layout.addWidget(self.storyboard_units[0])

        # self.setLayout(self.unit_layout)

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

class MainWindowController(QWidget):
    def __init__(self, toolbar_model, toolbar_view):
        super().__init__()

        self.toolbar_controller = ToolbarViewController(toolbar_model, toolbar_view)
        # story_board_container_controller = StoryBoardContainerViewController()

