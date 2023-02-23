from django.db import models
from codata_dw.base_models.base_model import ModelBase

class BaseSpreedsheets(ModelBase):
    spreedsheet = models.FileField()
    processed = models.BooleanField()
    version_used = models.CharField(max_length=50)

    class Meta:
        abstract = True