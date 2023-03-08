import pandas as pd
import numpy as np
from decimal import Decimal
from datetime import datetime
from typing import Any

from django.core.exceptions import ValidationError
from spreadsheet.base.processing_sheets import ProcessingSheets
from tributos.models import Iss
from tributos.models.choices import TIPO_SERVICO
from cnpj.models import CnpjCei



class ProcessingIssV1(ProcessingSheets):
    "Processar planilha de ISS"
    model = Iss
    df_formated: pd.DataFrame

    columns_to_drop = ["__rn"]
    choice_types: dict = {
        "TpServico": TIPO_SERVICO,
    }

    MONTHS_TO_PROCESS = {
        "Jan":1,
        "Fev":2,
        "Mar":3,
        "Abr":4,
        "Mai":5,
        "Jun":6,
        "Jul":7,
        "Ago":8,
        "Sete":9,
        "Out":10,
        "Nov":11,
        "Dez":12
    }
    default_columns = [
        'AnoReferencia',
        'SetorOrigem',
        'IdOrigem',
        'Cnpj',
        'Nome',
        'TpServico',
        'CodAtividade',
        'DescrAtividade',
        'BaseCalculo_Jan',
        'ISS_Jan',
        'BaseCalculo_Fev',
        'ISS_Fev',
        'BaseCalculo_Mar',
        'ISS_Mar',
        'BaseCalculo_Abr',
        'ISS_Abr',
        'BaseCalculo_Mai',
        'ISS_Mai',
        'BaseCalculo_Jun',
        'ISS_Jun',
        'BaseCalculo_Jul',
        'ISS_Jul',
        'BaseCalculo_Ago',
        'ISS_Ago',
        'BaseCalculo_Sete',
        'ISS_Sete',
        'BaseCalculo_Out',
        'ISS_Out',
        'BaseCalculo_Nov',
        'ISS_Nov',
        'BaseCalculo_Dez',
        'ISS_Dez',
        '__rn'
    ]

    def to_decimal(self, value: Any):
        try:
            return Decimal(value).quantize(Decimal("1.00"))
        except:
            return Decimal("0.0")
    
    def __format_df(self):
        self._check_columns()
        self.df = self.df.rename(columns=self.sheet_to_model)
        for i in self.default_columns[8:32]:
            self.df[i] = self.df[i].apply(self.to_decimal)
        self.df["Cnpj"] = self.df["Cnpj"].astype(str).apply(lambda x: x.replace(".", "").replace("/", "").replace("-", "").zfill(14))
        
        self.df = self.df.replace({np.nan: ""})
        self.df = self.df.replace({pd.NaT: None})
        self._get_choice()
        self._drop_columns()


    def __create_or_update(self, data: dict):
        cnpj_cei = data.pop("cnpj_cei")
        cnpj_cei_model = CnpjCei
        period = data.pop("period")
        cnae = data.pop("cod_atividade_cnae")
        cnpj_cei_model = self.model.objects.get(cnpj_cei=cnpj_cei, period=period, cod_atividade_cnae=cnae)
        self.models_to_update.append((cnpj_cei_model, data))

    def generate_df(self):
        new_rows = []
        # Dataframe formated with a row each period of iss
        for index, row in self.df.iterrows():
            for month in self.MONTHS_TO_PROCESS.keys():
                new_rows.append({
                    "cnpj_cei": row["Cnpj"],
                    "iss_value": row[f"ISS_{month}"],
                    "base_calculo": row[f"BaseCalculo_{month}"],
                    "period": datetime(int(row["AnoReferencia"]), self.MONTHS_TO_PROCESS[month], 1),
                    "cod_atividade_cnae": row["CodAtividade"],
                    "tipo_servico": row["TpServico"],
                    "descricao_atividade": row["DescrAtividade"]
                })
        # Dataframe formated with a row each period of iss
        return pd.DataFrame(new_rows)

    def is_valid(self) -> bool:
        self.errors = []
        df_formated: pd.DataFrame
        try:
            self.__format_df()
            df_formated = self.generate_df()
        except Exception as e:
            self.errors.append({"GenericError": str(e)})
            return False
        for index, row in df_formated.iterrows():
            try:
                row["cnpj_cei"] = CnpjCei.objects.get(identification_number=row["cnpj_cei"])
                model_to_check = self.model(**row)
                model_to_check.clean_fields()
                self.__create_or_update(row)
            except ValidationError as e:
                error = e.message_dict
                error["row"] = row.to_json()
                self.errors.append(error)
            except self.model.DoesNotExist as e:
                self.models_to_create.append(model_to_check)
            except CnpjCei.DoesNotExist as e:
                self.errors.append({"CnpjCei.DoesNotExist": row["cnpj_cei"]})
            except Exception as e:
                self.errors.append({"GenericError": str(e), "row": row.to_json()})

        if self.errors:
            return False

        return True
