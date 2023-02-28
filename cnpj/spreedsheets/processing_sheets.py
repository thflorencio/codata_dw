from abc import ABC
from typing import List
from django.db.models import Model, FileField
from pandas import DataFrame

class ProcessingSheets(ABC):
    spreedsheets: "Spreedsheets"
    model: Model
    models_to_create: List[Model] = []
    models_to_update: List[Model] = []
    # this dict is used to change name of collumns from Dataframe to save to Model
    # Ex. self.df = pd.read_excel(spreedsheet)
    sheet_to_model: dict = {}
    df: DataFrame
    errors: dict = []
    
    def __init__(self, spreedsheet: FileField) -> None: ...
    def is_valid(self) -> bool: ...

    def save(self) ->  None:
        if self.errors:
            raise Exception("Fix the error before save")
        
        self.model.objects.bulk_create(self.models_to_create)
        for model_to_update in self.models_to_update:
            model_to_update[0].update(**model_to_update[1])
