from django.db import models
from codata_dw.base_models.base_spreadsheet import BaseSpreadsheet
from spreadsheet.scripts import choices_spreadsheet_scripts


class Spreadsheet(BaseSpreadsheet):
    processor = models.CharField(max_length=250, choices=choices_spreadsheet_scripts())

    def __str__(self):
        return f"Status: {self.get_status_display()}"
