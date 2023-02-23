from abc import ABC
from cnpj.models.spreedsheets import Spreedsheets

class ProcessingSheets(ABC):
    spreedsheets: Spreedsheets
    

    def __init__(self, spreedsheet: Spreedsheets):
        self.spreedsheets = spreedsheet
        if not hasattr(self, 'model'):
            raise Exception("Is necessary a model to save spreedsheet")


    def save(self):
        ...

    def is_valid(self):
        ...

    
