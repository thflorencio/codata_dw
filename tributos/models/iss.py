from django.db import models
from codata_dw.utils.base_model import ModelBase
from tributos.models.choices.tipo_servico import TIPO_SERVICO

class Iss(ModelBase):
    cnpj_cei = models.ForeignKey('cnpj.CnpjCei', on_delete=models.CASCADE)
    iss_value = models.DecimalField("Valor ISS", max_digits=11, decimal_places=2)
    base_calculo =  models.DecimalField("Valor ISS", max_digits=11, decimal_places=2)
    period = models.DateField("Periodo de Apuracao", auto_now=False, auto_now_add=False)
    cod_atividade_cnae = models.CharField("Codigo da Atividade", max_length=5)
    tipo_servico = models.IntegerField("Tipo de Serviço", choices=TIPO_SERVICO)

    class Meta:
        verbose_name = "ISS"
        verbose_name_plural = "ISS"

    def __str__(self):
        return f"CNPJ: {self.cnpj.identification_number} BC: {self.base_calculo}, ISS: {self.iss_value}"
