from codata_dw.base_models.base_spreadsheet import BaseSpreadsheet
from cnpj.spreadsheet.processing_rfb_v1 import ProcessingRfbV1

class Spreadsheet(BaseSpreadsheet):

    def __str__(self):
        return f"Status: {self.get_status_display()}"

    def process(self):
        self.status = 1
        self.save()
        processing_rfb = ProcessingRfbV1(self.spreadsheet)
        if processing_rfb.is_valid():
            processing_rfb.save()
            self.status=3
        else:
            self.status = 2
            self.errors = processing_rfb.errors
            
        self.save()
        
