import typing

class MainModel:
    def __init__(self):
        self.description = None
        self.image_url = ''
        self.image_file_path = ''

class ImageDescriptionModel:
    def __init__(self):
        self.name = None
        self.description = None

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

class SettingsModel:
    def __init__(self):
        self.openai_api_key = None
        self.data_dir = None

# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------

class GptResultType:
    def __init__(self):
        self.question: typing.Optional[str] = None
        self.answer: typing.Optional[str] = None
        self.subject: typing.Optional[str] = None
        self.book: typing.Optional[str] = None
        self.chapter: typing.Optional[str] = None