from django.db import models

from codata_dw.base_models.base_model import ModelBase
from cnpj.models.choices import TIPOS, IDENTIFICACAO, SITUACAO_CADASTRAL, MOTIVO_SITUACAO, NATUREZA_JURIDICA, PORTE

class CnpjCei(ModelBase):

    ccm = models.CharField("CCM", max_length=10)
    name = models.CharField("Nome", max_length=250)
    fantasy_name = models.CharField("Nome Fantasia", max_length=250)
    phone = models.CharField("Telefone", max_length=50, null=True)
    identification_number = models.CharField("Número de Identificação", max_length=14)
    type_identification = models.IntegerField("Tipo", choices=TIPOS, null=True)
    identif_m_f = models.IntegerField("Identificacao M/F", choices=IDENTIFICACAO, null=True)
    situacao_cadastral = models.IntegerField("Situação Cadastral", choices=SITUACAO_CADASTRAL, null=True)
    motivo_situacao = models.IntegerField("Motivo Situação Cadastral", choices=MOTIVO_SITUACAO, null=True)
    natureza_juridica = models.IntegerField("Natureza Juridica", choices=NATUREZA_JURIDICA, null=True)
    porte = models.IntegerField("Porte", choices=PORTE, null=True)
    street = models.CharField("Logradouro", max_length=250)
    street_number = models.CharField("Numero", max_length=10)
    neighborhood = models.CharField("Bairro", max_length=50)
    complement_address = models.CharField("Complemento", max_length=50)
    zipcode = models.CharField("Código Postal", max_length=8)
    state = models.CharField("Estado", max_length=2)
    main_cnae = models.CharField("Principal CNAE", max_length=10)

    @property
    def identification_number_raiz(self):
        if self.type_identification == 1 or self.type_identification == 2:
            return "0"
        return self.identification_number[0:8].lstrip("0")

    def __str__(self):
        return f"{self.get_type_identification_display()}: {self.identification_number}"

    class Meta:
        managed = True
        verbose_name = "CnpjCei"
        verbose_name_plural = "CnpjCeis"
