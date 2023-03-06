from cnpj.spreadsheet import ProcessingRfbV1

SPREADSHEET_SCRIPTS = {
    "rfb_v1": ProcessingRfbV1
}

def choices_spreadsheet_scripts():
    choices = [(k, k) for k in SPREADSHEET_SCRIPTS.keys()]
    return tuple(choices)