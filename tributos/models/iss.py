from django.db import models
from codata_dw.base_models.base_model import ModelBase
from tributos.models.choices.tipo_servico import TIPO_SERVICO


class Iss(ModelBase):
    identification_number = models.CharField("Número de Identificação", max_length=14)
    iss_value = models.DecimalField("Valor ISS", max_digits=20, decimal_places=2)
    base_calculo = models.DecimalField("Base de Calculo", max_digits=20, decimal_places=2)
    period = models.DateField("Periodo de Apuracao", auto_now=False, auto_now_add=False)
    cod_atividade_cnae = models.CharField("Codigo da Atividade", max_length=8, null=True, blank=True)
    tipo_servico = models.IntegerField("Tipo de Serviço", choices=TIPO_SERVICO, null=True, blank=True)
    descricao_atividade = models.TextField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['identification_number', 'period', 'cod_atividade_cnae']),
            ]
        verbose_name = "ISS"
        verbose_name_plural = "ISS"

    def __str__(self):
        return f"BC: {self.base_calculo}, ISS: {self.iss_value}"
