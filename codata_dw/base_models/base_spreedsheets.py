from uuid import uuid4
from django.db import models
from codata_dw.base_models.base_model import ModelBase

def file_name(instance, filename):
    return '/'.join(['spreedsheet', str(instance.pk), filename])

class BaseSpreedsheets(ModelBase):
    
    STATUS = (
        (0, "Enviado"),
        (1, "Processando"),
        (2, "Erro"),
        (3, "Processado com Sucesso"))
    spreedsheet = models.FileField(upload_to=file_name)
    status = models.IntegerField(choices=STATUS, default=0)
    version_used = models.CharField(max_length=50)
    errors = models.JSONField(null=True)

    class Meta:
        abstract = True