import pandas as pd
import numpy as np

from django.core.exceptions import ValidationError
from cnpj.spreedsheets.processing_sheets import ProcessingSheets
from cnpj.models import CnpjCei
from cnpj.models.choices import IDENTIFICACAO, NATUREZA_JURIDICA, PORTE, SITUACAO_CADASTRAL, MOTIVO_SITUACAO
from cnpj.models.choices.utils import get_key_by_value


class ProcessingRfbV1(ProcessingSheets):
    "Processar planilha de CNPJ da Receita Federal do Brasil"
    model = CnpjCei
    sheet_to_model = {
       "CNPJ": "identification_number",
       "IDENTIF M/F": "identif_m_f",
       "NOME EMPRESARIAL": "name",
       "NOME FANTASIA": "fantasy_name",
       "NATUREZA JURIDICA": "legal_nature",
       "PORTE": "company_size",
       "CAPITAL SOCIAL": "social_capital",
       "SITUAÇÃO CADASTRAL": "registration_status",
       "DATA SITUAÇÃO": "date_registration_status",
       "MOTIVO DA SITUAÇÃO": "reason_situation",
       "INICIO ATIV": "start_activities",
       "CNAE PRINCIPAL": "main_cnae",
       "LOGRADOURO": "street",
       "NUMERO": "street_number",
       "COMPL": "complement_address",
       "BAIRRO": "neighborhood",
       "CEP": "zipcode",
       "UF": "state",
       "TELEFONE": "phone",
       "TELEFONE2": "phone2"
    }

    def __get_choice(self, row, type_choice):

        types: dict = {
            "identif_m_f": IDENTIFICACAO,
            "legal_nature": NATUREZA_JURIDICA,
            "company_size": PORTE,
            "registration_status":SITUACAO_CADASTRAL,
            "reason_situation": MOTIVO_SITUACAO
        }

        return get_key_by_value(types[type_choice], row[type_choice])

    def __format_df(self):
        self.df = self.df.replace({np.nan:""})
        self.df["LOGRADOURO"] = self.df["TP LOGRAD"].astype(str) + " " + self.df["LOGRADOURO"].astype(str)
        self.df["TELEFONE"] = self.df["DDD 1"].astype(str) + self.df["TELEFONE 1"].astype(str)
        self.df["TELEFONE2"] = self.df["DDD 2"].astype(str) + self.df["TELEFONE 2"].astype(str)
        self.df["type_identification"] = 0
        self.df = self.df.drop(columns=["DDD FAX", "FAX", "CNAE SECUNDARIA", "CNPJ BASE", "DDD 1", "TELEFONE 1", "DDD 2", "TELEFONE 2", "TP LOGRAD"], axis=0)
        self.df["INICIO ATIV"]  = pd.to_datetime(self.df["INICIO ATIV"], format="%Y%m%d")
        self.df["DATA SITUAÇÃO"]  = pd.to_datetime(self.df["DATA SITUAÇÃO"], format="%Y%m%d")
        self.df = self.df.rename(columns=self.sheet_to_model)
        self.df["identif_m_f"] = self.df.apply(self.__get_choice, axis=1, args=("identif_m_f",))
        self.df["legal_nature"] = self.df.apply(self.__get_choice, axis=1, args=("legal_nature",))
        self.df["company_size"] = self.df.apply(self.__get_choice, axis=1, args=("company_size",))
        self.df["registration_status"] = self.df.apply(self.__get_choice, axis=1, args=("registration_status",))
        self.df["reason_situation"] = self.df.apply(self.__get_choice, axis=1, args=("reason_situation",))

    def __init__(self, spreedsheet: "FileField") -> None:
        self.spreedsheets = spreedsheet
        self.df = pd.read_excel(spreedsheet, decimal=",")
        self.__format_df()

    def __create_or_update(self, data: dict):
        identification_number = data.pop('identification_number')
        cnpj_cei = self.model.objects.get(identification_number=identification_number)
        self.models_to_update.append((cnpj_cei, data))
        

    def is_valid(self) -> bool:
        self.errors = []
        for index, row in self.df.iterrows():
            try:
                model_to_check = self.model(**row)
                model_to_check.clean_fields()
                self.__create_or_update(row)
                
            except ValidationError as e:
                self.errors.append(e.message_dict)
            except CnpjCei.DoesNotExist as e:
                self.models_to_create.append(model_to_check)
            except Exception as e:
                self.errors.append({"GenericError": str(e)})

        if self.errors:
            return False
        
        return True
