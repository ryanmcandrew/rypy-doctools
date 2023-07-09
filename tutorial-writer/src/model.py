import typing

class Chapter:
    def __init__(self):
        self._name = None
        self._target_characters_per_subject = None
        self._subjects = None
        self._helper_prompt_head = None
        self._helper_prompt_tail = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property 
    def target_characters_per_subject(self):
        return self._target_characters_per_subject
    
    @target_characters_per_subject.setter 
    def target_characters_per_subject(self, value):
        self._target_characters_per_subject = value
    
    @property
    def subjects(self):
        return self._subjects
    
    @subjects.setter
    def subjects(self, value):
        self._subjects = value
    
    @property
    def helper_prompt_head(self):
        return self._helper_prompt_head
    
    @helper_prompt_head.setter
    def helper_prompt_head(self, value):
        self._helper_prompt_head = value
    
    @property
    def helper_prompt_tail(self):
        return self._helper_prompt_tail
    
    @helper_prompt_tail.setter
    def helper_prompt_tail(self, value):
        self._helper_prompt_tail = value

class Book:
    def __init__(self):
        self._chapters: typing.List[Chapter] = []
        self._name: str = None

    @property
    def chapters(self):
        return self._chapters

    def append_decorator(function):
        def wrapper(self, *args, **kwargs):
            value = function(self, *args, **kwargs)
            self._chapters.append(value)
            return value
        return wrapper
    
    @append_decorator
    def append_chapter(self, value):
        return value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

class GptResultType:
    def __init__(self):
        self.question: typing.Optional[str] = None
        self.answer: typing.Optional[str] = None
        self.subject: typing.Optional[str] = None
        self.book: typing.Optional[str] = None
        self.chapter: typing.Optional[str] = None
