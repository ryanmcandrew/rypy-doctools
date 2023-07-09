class Model:
    def __init__(self):
        self.text = ""

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text
    
class ToolbarModel:
    def __init__(self):
        self.state = ""

class CharacterUnitModel:
    def __init__(self):
        self.name = None
        self.species = None
        self.traits = None
        self.abilities = None
        self.development = None
        self.occupation = None
        self.interests = None
        self.habits = None
        self.outfit = None
        self.face = None
        self.body_type = None
        self.background = None
        self.relationships = None
        self.age = None
        self.beliefs = None
        self.home_type = None
        self.is_hero = None
        self.is_villain = None

        self.equipment = None
        self.aspirations = None

class EnvironmentUnitModel:
    def __init__(self):
        self.name = None
        self.biome = None
        self.details = None

class EventUnitModel:
    pass

class DialogueUnitModel:
    def __init__(self):
        self.name = None
        self.biome = None
        self.details = None

class PlotUnitModel:
    def __init__(self):
        self.name = None
        self.details = None

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

class CharacterContainerModel:
    def __init__(self):
        pass

class EnvironmentContainerModel:
    def __init__(self):
        self.name = None
        self.biome = None
        self.details = None

class EventContainerModel:
    pass

class DialogueContainerModel:
    def __init__(self):
        self.name = None
        self.biome = None
        self.details = None

class PlotContainerModel:
    def __init__(self):
        self.name = None
        self.details = None

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

class SettingsModel:
    def __init__(self):
        self.openai_api_key = None

class MainWindowModel:
    def __init__(self):
        pass