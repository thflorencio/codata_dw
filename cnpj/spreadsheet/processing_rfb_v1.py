import pandas as pd
import numpy as np
from decimal import Decimal

from django.core.exceptions import ValidationError
from spreadsheet.base.processing_sheets import ProcessingSheets
from cnpj.models import CnpjCei
from cnpj.models.choices import (
    IDENTIFICACAO,
    NATUREZA_JURIDICA,
    PORTE,
    SITUACAO_CADASTRAL,
    MOTIVO_SITUACAO,
    TYPES_STREET,
)


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
        "TP LOGRAD": "type_street",
        "LOGRADOURO": "street",
        "NUMERO": "street_number",
        "COMPL": "complement_address",
        "BAIRRO": "neighborhood",
        "CEP": "zipcode",
        "UF": "state",
        "DDD 1": "ddd_phone",
        "TELEFONE 1": "phone",
        "DDD 2": "ddd_phone2",
        "TELEFONE 2": "phone2",
    }
    columns_to_drop = ["DDD FAX", "FAX", "CNAE SECUNDARIA", "CNPJ BASE"]
    choice_types: dict = {
        "identif_m_f": IDENTIFICACAO,
        "legal_nature": NATUREZA_JURIDICA,
        "company_size": PORTE,
        "registration_status": SITUACAO_CADASTRAL,
        "reason_situation": MOTIVO_SITUACAO,
        "type_street": TYPES_STREET,
    }
    default_columns = [
        "CNPJ",
        "IDENTIF M/F",
        "CNPJ BASE",
        "NOME EMPRESARIAL",
        "NOME FANTASIA",
        "NATUREZA JURIDICA",
        "PORTE",
        "CAPITAL SOCIAL",
        "SITUAÇÃO CADASTRAL",
        "DATA SITUAÇÃO",
        "MOTIVO DA SITUAÇÃO",
        "INICIO ATIV",
        "CNAE PRINCIPAL",
        "CNAE SECUNDARIA",
        "TP LOGRAD",
        "LOGRADOURO",
        "NUMERO",
        "COMPL",
        "BAIRRO",
        "CEP",
        "UF",
        "DDD 1",
        "TELEFONE 1",
        "DDD 2",
        "TELEFONE 2",
        "DDD FAX",
        "FAX",
    ]

    def __format_df(self):
        self._check_columns()
        self.df = self.df.rename(columns=self.sheet_to_model)
        self.df["start_activities"] = pd.to_datetime(
            self.df["start_activities"], format="%Y%m%d", errors="coerce"
        )
        self.df["date_registration_status"] = pd.to_datetime(
            self.df["date_registration_status"], format="%Y%m%d", errors="coerce"
        )
        self.df["social_capital"] = self.df["social_capital"].apply(
            lambda x: Decimal(x).quantize(Decimal("1.00"))
        )
        self.df[["ddd_phone", "phone", "ddd_phone2", "phone2"]] = self.df[
            ["ddd_phone", "phone", "ddd_phone2", "phone2"]
        ].fillna(0)
        self.df[["ddd_phone", "phone", "ddd_phone2", "phone2"]] = self.df[
            ["ddd_phone", "phone", "ddd_phone2", "phone2"]
        ].astype(int, errors="ignore")
        self.df["zipcode"] = self.df["zipcode"].astype(str).str.zfill(8)
        self.df["identification_number"] = (
            self.df["identification_number"].astype(str).str.zfill(14)
        )
        self.df["type_identification"] = 0
        self.df = self.df.replace({np.nan: ""})
        self.df = self.df.replace({pd.NaT: None})
        self._get_choice()
        self._drop_columns()

    def __init__(self, spreadsheet: "FileField") -> None:
        self.df = pd.read_excel(spreadsheet, decimal=",", sheet_name="ESTABELECIMENTO")

    def __create_or_update(self, data: dict):
        identification_number = data.pop("identification_number")
        cnpj_cei = self.model.objects.get(identification_number=identification_number)
        self.models_to_update.append((cnpj_cei, data))

    def is_valid(self) -> bool:
        self.errors = []
        try:
            self.__format_df()
        except Exception as e:
            self.errors.append({"GenericError": str(e)})
            return False

        for index, row in self.df.iterrows():
            try:
                model_to_check = self.model(**row)
                model_to_check.clean_fields()
                self.__create_or_update(row)

            except ValidationError as e:
                error = e.message_dict
                error["row"] = row.to_json()
                self.errors.append(error)
            except CnpjCei.DoesNotExist as e:
                self.models_to_create.append(model_to_check)
            except Exception as e:
                self.errors.append({"GenericError": str(e), "row": row.to_json()})

        if self.errors:
            return False

        return True
