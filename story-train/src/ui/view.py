import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QLineEdit, QPushButton, QPlainTextEdit
from PyQt5.QtWidgets import QLabel, QToolBar
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QPixmap

class ToolbarView(QWidget):
    def __init__(self):
        super().__init__()

        self.home_button = QPushButton("Home")
        self.characters_button = QPushButton("Characters")
        self.environment_button = QPushButton("Environment")
        self.event_button = QPushButton("Event")
        self.dialogue_button = QPushButton("Dialogue")
        self.settings_button = QPushButton("Settings")

        layout = QVBoxLayout()
        layout.addWidget(self.home_button)
        layout.addWidget(self.characters_button)
        layout.addWidget(self.environment_button)
        layout.addWidget(self.event_button)
        layout.addWidget(self.dialogue_button)
        layout.addWidget(self.settings_button)

        self.setLayout(layout)

class SettingsView(QWidget):
    def __init__(self):
        super().__init__()


        self.api_key_label = QLabel("Openai API key")
        self.api_key = QLineEdit()

        layout = QVBoxLayout()
        # layout.addWidget(self.name_input_box)
        # layout.addWidget(self.trait_input_box)
        layout.addWidget(self.api_key_label)
        layout.addWidget(self.api_key)

        self.setLayout(layout)

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

class CharacterUnitView(QWidget):
    def __init__(self):
        super().__init__()

        self.uid_control_label = QLabel("UID")
        self.uid_control = QLineEdit()
        self.name_control_label = QLabel("Name")
        self.name_control = QLineEdit()
        self.species_control_label = QLabel("Species")
        self.species_control = QLineEdit()
        self.traits_control_label = QLabel("Traits")
        self.traits_control = QLineEdit()
        self.abilities_control_label = QLabel("Abilities")
        self.abilities_control = QLineEdit()
        self.aspirations_control_label = QLabel("Aspirations")
        self.aspirations_control = QLineEdit()
        self.development_control_label = QLabel("Development")
        self.development_control = QLineEdit()
        self.occupation_control_label = QLabel("Occupation")
        self.occupation_control = QLineEdit()
        self.interests_control_label = QLabel("Interests")
        self.interests_control = QLineEdit()
        self.habits_control_label = QLabel("Habits")
        self.habits_control = QLineEdit()
        self.outfit_control_label = QLabel("Outfit")
        self.outfit_control = QLineEdit()
        self.face_control_label = QLabel("Face")
        self.face_control = QLineEdit()
        self.body_type_control_label = QLabel("Body Type")
        self.body_type_control = QLineEdit()
        self.background_control_label = QLabel("Background")
        self.background_control = QLineEdit()
        self.relationships_control_label = QLabel("Relationships")
        self.relationships_control = QLineEdit()
        self.age_control_label = QLabel("Age")
        self.age_control = QLineEdit()
        self.beliefs_control_label = QLabel("Beliefs")
        self.beliefs_control = QLineEdit()
        self.home_type_control_label = QLabel("Home Type")
        self.home_type_control = QLineEdit()
        self.is_hero_control_label = QLabel("Is Hero")
        self.is_hero_control = QLineEdit()
        self.is_villain_control_label = QLabel("Is Villain")
        self.is_villain_control = QLineEdit()
        
        self.unit_layout = QVBoxLayout()

        self.unit_layout.addWidget(self.uid_control_label)
        self.unit_layout.addWidget(self.uid_control)
        self.unit_layout.addWidget(self.name_control_label)
        self.unit_layout.addWidget(self.name_control)
        self.unit_layout.addWidget(self.species_control_label)
        self.unit_layout.addWidget(self.species_control)
        self.unit_layout.addWidget(self.traits_control_label)
        self.unit_layout.addWidget(self.traits_control)
        self.unit_layout.addWidget(self.abilities_control_label)
        self.unit_layout.addWidget(self.abilities_control)
        self.unit_layout.addWidget(self.aspirations_control_label)
        self.unit_layout.addWidget(self.aspirations_control)
        self.unit_layout.addWidget(self.development_control_label)
        self.unit_layout.addWidget(self.development_control)
        self.unit_layout.addWidget(self.occupation_control_label)
        self.unit_layout.addWidget(self.occupation_control)
        self.unit_layout.addWidget(self.interests_control_label)
        self.unit_layout.addWidget(self.interests_control)
        self.unit_layout.addWidget(self.habits_control_label)
        self.unit_layout.addWidget(self.habits_control)
        self.unit_layout.addWidget(self.outfit_control_label)
        self.unit_layout.addWidget(self.outfit_control)
        self.unit_layout.addWidget(self.face_control_label)
        self.unit_layout.addWidget(self.face_control)
        self.unit_layout.addWidget(self.body_type_control_label)
        self.unit_layout.addWidget(self.body_type_control)
        self.unit_layout.addWidget(self.background_control_label)
        self.unit_layout.addWidget(self.background_control)
        self.unit_layout.addWidget(self.relationships_control_label)
        self.unit_layout.addWidget(self.relationships_control)
        self.unit_layout.addWidget(self.age_control_label)
        self.unit_layout.addWidget(self.age_control)
        self.unit_layout.addWidget(self.beliefs_control_label)
        self.unit_layout.addWidget(self.beliefs_control)
        self.unit_layout.addWidget(self.home_type_control_label)
        self.unit_layout.addWidget(self.home_type_control)
        self.unit_layout.addWidget(self.is_hero_control_label)
        self.unit_layout.addWidget(self.is_hero_control)
        self.unit_layout.addWidget(self.is_villain_control_label)
        self.unit_layout.addWidget(self.is_villain_control)

        self.setLayout(self.unit_layout)

class EnvironmentUnitView(QWidget):
    def __init__(self):
        super().__init__()

        self.name_control_label = QLabel("Name")
        self.name_control = QLineEdit()
        self.biome_control_label = QLabel("Biome")
        self.biome_control = QLineEdit()
        self.details_control_label = QLabel("Details")
        self.details_control = QLineEdit()

        layout = QVBoxLayout()

        layout.addWidget(self.name_control_label)
        layout.addWidget(self.name_control)
        layout.addWidget(self.biome_control_label)
        layout.addWidget(self.biome_control)
        layout.addWidget(self.details_control_label)
        layout.addWidget(self.details_control)

        self.setLayout(layout)

class EventUnitView(QWidget):
    def __init__(self):
        super().__init__()

        self.name_control_label = QLabel("Name")
        self.name_control = QLineEdit()
        self.conflict_control_label = QLabel("Conflict")
        self.conflict_control = QLineEdit()
        self.goal_control_label = QLabel("Goal")
        self.goal_control = QLineEdit()
        self.rising_action_control_label = QLabel("Rising Action")
        self.rising_action_control = QLineEdit()
        self.climax_control_label = QLabel("Climax")
        self.climax_control = QLineEdit()
        self.resolution_control_label = QLabel("Resolution")
        self.resolution_control = QLineEdit()
        self.subplot_control_label = QLabel("Subplot")
        self.subplot_control = QLineEdit()
        self.theme_control_label = QLabel("Theme")
        self.theme_control = QLineEdit()
        self.twist_control_label = QLabel("Twist")
        self.twist_control = QLineEdit()

        layout = QVBoxLayout()

        layout.addWidget(self.name_control_label)
        layout.addWidget(self.name_control)
        layout.addWidget(self.conflict_control_label)
        layout.addWidget(self.conflict_control)
        layout.addWidget(self.goal_control_label)
        layout.addWidget(self.goal_control)
        layout.addWidget(self.rising_action_control_label)
        layout.addWidget(self.rising_action_control)
        layout.addWidget(self.climax_control_label)
        layout.addWidget(self.climax_control)
        layout.addWidget(self.resolution_control_label)
        layout.addWidget(self.resolution_control)
        layout.addWidget(self.subplot_control_label)
        layout.addWidget(self.subplot_control)
        layout.addWidget(self.theme_control_label)
        layout.addWidget(self.theme_control)
        layout.addWidget(self.twist_control_label)
        layout.addWidget(self.twist_control)

        self.setLayout(layout)

class DialogueUnitView(QWidget):
    def __init__(self):
        super().__init__()

        self.name_control_label = QLabel("Name")
        self.name_control = QLineEdit()
        self.characters_control_label = QLabel("Characters")
        self.characters_control = QLineEdit()
        self.details_control_label = QLabel("Details")
        self.details_control = QLineEdit()

        layout = QVBoxLayout()

        layout.addWidget(self.name_control_label)
        layout.addWidget(self.name_control)
        layout.addWidget(self.characters_control_label)
        layout.addWidget(self.characters_control)
        layout.addWidget(self.details_control_label)
        layout.addWidget(self.details_control)

        self.setLayout(layout)

class StoryBoardUnitView(QWidget):
    def __init__(self):
        super().__init__()

        self.image = None
        self.description = QPlainTextEdit(self)
        self.dialogue = QPlainTextEdit(self)

        self.pix = QPixmap('src/static/question.jpg')
        self.pix_label = QLabel()
        self.pix_label.setPixmap(self.pix)
        # self.pix_label.resize(10,10)

        self.unit_layout = QVBoxLayout()
        self.unit_layout.addWidget(self.pix_label)
        self.unit_layout.addWidget(self.description)
        self.unit_layout.addWidget(self.dialogue)

        self.setLayout(self.unit_layout)

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

class CharacterContainerView(QWidget):
    def __init__(self):
        super().__init__()

        self.character_units = []
        self.character_units.append(CharacterUnitView())

        self.add_character_control = QPushButton("Add Character")
        self.add_character_control.clicked.connect(self.append_character)

        self.unit_layout = QVBoxLayout()
        self.unit_layout.addWidget(self.character_units[0])
        self.unit_layout.addWidget(self.add_character_control)

        self.setLayout(self.unit_layout)

    def append_character(self):
        self.unit_layout.removeWidget(self.add_character_control)
        self.unit_layout.addWidget(CharacterUnitView())
        self.unit_layout.addWidget(self.add_character_control)
        self.setLayout(self.unit_layout)


class EnvironmentContainerView(QWidget):
    def __init__(self):
        super().__init__()

        self.environment_units = []
        self.environment_units.append(EnvironmentUnitView())

        self.add_environment_control = QPushButton("Add Environment")

        self.add_environment_control.clicked.connect(self.add_environment)

        self.unit_layout = QVBoxLayout()
        self.unit_layout.addWidget(self.environment_units[0])
        self.unit_layout.addWidget(self.add_environment_control)

        self.setLayout(self.unit_layout)

    def add_environment(self):
        self.unit_layout.removeWidget(self.add_environment_control)
        self.unit_layout.addWidget(EnvironmentUnitView())
        self.unit_layout.addWidget(self.add_environment_control)
        self.setLayout(self.unit_layout)

class EventContainerView(QWidget):
    def __init__(self):
        super().__init__()

        self.event_units = []
        self.event_units.append(EventUnitView())

        self.add_event_control = QPushButton("Add Event")

        self.add_event_control.clicked.connect(self.append_event)


        self.unit_layout = QVBoxLayout()
        self.unit_layout.addWidget(self.event_units[0])
        self.unit_layout.addWidget(self.add_event_control)

        self.setLayout(self.unit_layout)

    def append_event(self):
        self.unit_layout.removeWidget(self.add_event_control)
        self.unit_layout.addWidget(EventUnitView())
        self.unit_layout.addWidget(self.add_event_control)
        self.setLayout(self.unit_layout)


class DialogueContainerView(QWidget):
    def __init__(self):
        super().__init__()

        self.dialogue_units = []
        self.dialogue_units.append(DialogueUnitView())

        self.add_dialogue_control = QPushButton("Add Dialogue")

        self.add_dialogue_control.clicked.connect(self.append_dialogue)

        self.unit_layout = QVBoxLayout()
        self.unit_layout.addWidget(self.dialogue_units[0])
        self.unit_layout.addWidget(self.add_dialogue_control)

        self.setLayout(self.unit_layout)

    def append_dialogue(self):
        print('test')
        self.unit_layout.removeWidget(self.add_dialogue_control)
        self.unit_layout.addWidget(DialogueUnitView())
        self.unit_layout.addWidget(self.add_dialogue_control)
        self.setLayout(self.unit_layout)

class StoryBoardContainerView(QWidget):
    def __init__(self):
        super().__init__()

        self.storyboard_units = []

        self.storyboard_units.append(StoryBoardUnitView())
        # self.storyboard_units.append(StoryBoardUnitView())

        self.unit_layout = QVBoxLayout()
        # self.unit_layout.addWidget(self.storyboard_units[0])
        for i in self.storyboard_units:
            self.unit_layout.addWidget(i)

        self.setLayout(self.unit_layout)

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

class MainWindowView(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.toolbar = ToolbarView()
        self.storyboard = StoryBoardContainerView()
        self.character_settings = CharacterContainerView()
        self.environment_settings = EnvironmentContainerView()
        self.dialogue_settings = DialogueContainerView()
        self.plot_settings = EventContainerView()
        self.settings = SettingsView()

        self.setWindowTitle("story train")

        
        toolbar = self.addToolBar('Toolbar e')
        editToolbar = QToolBar()
        toolbar.setOrientation(1)

        home_action = QAction('Story Board', self)
        character_action = QAction('Characters', self)
        environment_action = QAction('Environments', self)
        dialogues_action = QAction('Dialogues', self)
        plot_action = QAction('Plots', self)
        settings_action = QAction('Settings', self)

        home_action.triggered.connect(self.show_homescreen)
        character_action.triggered.connect(self.show_character)
        environment_action.triggered.connect(self.show_environment)
        dialogues_action.triggered.connect(self.show_dialogue)
        plot_action.triggered.connect(self.show_plot)
        settings_action.triggered.connect(self.show_settings)

        editToolbar.addAction(home_action)
        editToolbar.addAction(character_action)
        editToolbar.addAction(environment_action)
        editToolbar.addAction(dialogues_action)
        editToolbar.addAction(plot_action)
        editToolbar.addAction(settings_action)
        toolbar.addWidget(editToolbar)
        

        # mainLayout = QVBoxLayout()
        # mainLayout.addWidget(self.toolbar)
        # mainLayout.addWidget(self.storyboard)

        self.stack = QStackedWidget()

        self.stack.addWidget(self.storyboard)
        self.stack.addWidget(self.character_settings)
        self.stack.addWidget(self.environment_settings)
        self.stack.addWidget(self.dialogue_settings)
        self.stack.addWidget(self.plot_settings)
        self.stack.addWidget(self.settings)

        self.setCentralWidget(self.stack)

        # self.setLayout(mainLayout)

        self.home_button = QPushButton("Home")
        self.characters_button = QPushButton("Characters")
        self.environment_button = QPushButton("Environment")
        self.event_button = QPushButton("Event")
        self.dialogue_button = QPushButton("Dialogue")
        self.settings_button = QPushButton("Settings")

    def show_homescreen(self):
        self.stack.setCurrentIndex(0)

    def show_character(self):
        self.stack.setCurrentIndex(1)

    def show_environment(self):
        self.stack.setCurrentIndex(2)

    def show_dialogue(self):
        self.stack.setCurrentIndex(3)

    def show_plot(self):
        self.stack.setCurrentIndex(4)

    def show_settings(self):
        self.stack.setCurrentIndex(5)