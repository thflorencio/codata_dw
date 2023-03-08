from abc import ABC
from typing import List
from django.db.models import Model, FileField
from pandas import DataFrame, read_excel
from cnpj.models.choices.utils import get_key_by_value


class ProcessingSheets(ABC):
    spreadsheet: "Spreadsheet"
    model: Model
    models_to_create: List[Model] = []
    models_to_update: List[Model] = []
    columns_to_drop: List[str] = []
    default_columns: List[str] = []

    # this dict is used to change name of collumns from Dataframe to save to Model
    sheet_to_model: dict = {}
    df: DataFrame
    errors: dict = []
    choice_types: dict

    def __init__(self, spreadsheet: "FileField") -> None:
        self.df = read_excel(spreadsheet, decimal=",")
        self.models_to_create = []
        self.models_to_update = []

    def is_valid(self) -> bool:
        ...

    def _drop_columns(self):
        self.df = self.df.drop(columns=self.columns_to_drop, axis=0)

    def _get_choice(self):
        for key in self.choice_types.keys():
            self.df[key] = self.df[key].apply(
                lambda x: get_key_by_value(self.choice_types[key], x)
            )

    def _check_columns(self):
        if sorted(self.default_columns) != sorted(self.df.columns.values.tolist()):
            raise Exception(f"Erro em Colunas, esperado {self.default_columns}")

    def save(self) -> None:
        if self.errors:
            raise Exception("Fix the error before save")
        
        self.model.objects.bulk_create(self.models_to_create, batch_size=1000)
        for model_to_update in self.models_to_update:
            model_to_update[0].update(**model_to_update[1])
