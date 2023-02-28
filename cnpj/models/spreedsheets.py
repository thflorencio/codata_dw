from codata_dw.base_models.base_spreedsheets import BaseSpreedsheets
from cnpj.spreedsheets.processing_rfb_v1 import ProcessingRfbV1

class Spreedsheets(BaseSpreedsheets):

    def __str__(self):
        return f"Procesed: {self.processed}"

    def process(self):
        self.status = 1
        self.save()
        processing_rfb = ProcessingRfbV1(self.spreedsheet)
        if processing_rfb.is_valid():
            processing_rfb.save()
            self.status=3
        else:
            self.status = 2
            self.errors = processing_rfb.errors
            
        self.save()
        
