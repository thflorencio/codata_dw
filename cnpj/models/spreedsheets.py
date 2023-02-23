from codata_dw.base_models.base_spreedsheets import BaseSpreedsheets
from cnpj.spreedsheets.processing_rfb_v1 import ProcessingRbfV1

class Spreedsheets(BaseSpreedsheets):

    def __str__(self):
        return f"Procesed: {self.processed}"

    def process(self):
        ...
