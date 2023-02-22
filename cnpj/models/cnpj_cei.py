from django.db import models


class CnpjCei(models.Model):
    TIPOS: tuple = ((0, "CNPJ"), (1, "CEI"), (2, "CAEPF"))

    identification_number = models.CharField("Numero de Identificação", max_length=14)
    type_identification = models.IntegerField("Tipo", choices=TIPOS)
    address = models.TextField("Endereço")

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
