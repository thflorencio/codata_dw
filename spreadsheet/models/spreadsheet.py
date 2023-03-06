from django.db import models
from codata_dw.base_models.base_spreadsheet import BaseSpreadsheet
from cnpj.spreadsheet.processing_rfb_v1 import ProcessingRfbV1
from spreadsheet.scripts import choices_spreadsheet_scripts, SPREADSHEET_SCRIPTS



class Spreadsheet(BaseSpreadsheet):
    processor = models.CharField(max_length=250, choices=choices_spreadsheet_scripts())

    def __str__(self):
        return f"Status: {self.get_status_display()}"

    def process(self):
        self.status = 1
        self.save()
        try:
            processing_rfb = SPREADSHEET_SCRIPTS[self.processor](self.spreadsheet)
        except KeyError:
            self.errors = {"erro": f"Processador {self.processor} não encontrdo"}
            self.save()
            return

        if processing_rfb.is_valid():
            processing_rfb.save()
            self.status = 3
        else:
            self.status = 2
            self.errors = processing_rfb.errors

        self.save()
