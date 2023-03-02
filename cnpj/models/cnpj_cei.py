from django.db import models

from codata_dw.base_models.base_model import ModelBase
from cnpj.models.choices import TIPOS, IDENTIFICACAO, SITUACAO_CADASTRAL, MOTIVO_SITUACAO, NATUREZA_JURIDICA, PORTE, TYPES_STREET

class CnpjCei(ModelBase):

    ccm = models.CharField("CCM", max_length=10, null=True, blank=True)
    identification_number = models.CharField("Número de Identificação", max_length=14)
    identif_m_f = models.IntegerField("Identificacao M/F", choices=IDENTIFICACAO, null=True, blank=True)
    name = models.CharField("Nome", max_length=250)
    fantasy_name = models.CharField("Nome Fantasia", max_length=250, null=True, blank=True)
    legal_nature = models.IntegerField("Natureza Juridica", choices=NATUREZA_JURIDICA, null=True, blank=True)
    company_size = models.IntegerField("Porte", choices=PORTE, null=True, blank=True)
    social_capital = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    registration_status = models.IntegerField("Situação Cadastral", choices=SITUACAO_CADASTRAL, null=True, blank=True)
    date_registration_status = models.DateField("Data do Status do Registro", null=True, blank=True)
    reason_situation = models.IntegerField("Motivo Situação Cadastral", choices=MOTIVO_SITUACAO, null=True, blank=True)
    start_activities =  models.DateField("Inicio das Atividades", null=True, blank=True)
    main_cnae = models.CharField("Principal CNAE", max_length=10, null=True, blank=True)
    type_street = models.IntegerField("Tipo de Logradouro", choices=TYPES_STREET, null=True, blank=True)
    street = models.CharField("Logradouro", max_length=250, null=True, blank=True)
    street_number = models.CharField("Numero", max_length=10, null=True, blank=True)
    complement_address = models.CharField("Complemento", max_length=250, null=True, blank=True)
    neighborhood = models.CharField("Bairro", max_length=50, null=True, blank=True)
    zipcode = models.CharField("Código Postal", max_length=8, null=True, blank=True)
    state = models.CharField("Estado", max_length=2, null=True, blank=True)
    ddd_phone = models.CharField("DDD Telefone", max_length=3, null=True, blank=True)
    phone = models.CharField("Telefone", max_length=50, null=True, blank=True)
    ddd_phone2 = models.CharField("DDD Telefone 2", max_length=3, null=True, blank=True)
    phone2 = models.CharField("Telefone 2", max_length=50, null=True, blank=True)
    type_identification = models.IntegerField("Tipo", choices=TIPOS, null=True, blank=True)
    

    class Meta:
        managed = True
        verbose_name = "CnpjCei"
        verbose_name_plural = "CnpjCeis"
        indexes = [
            models.Index(fields=['identification_number']),
        ]

    @property
    def identification_number_raiz(self):
        if self.type_identification == 1 or self.type_identification == 2:
            return "0"
        return self.identification_number[0:8].lstrip("0")

    def __str__(self):
        return f"{self.get_type_identification_display()}: {self.identification_number}"
