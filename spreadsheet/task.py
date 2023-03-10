from datetime import datetime
from codata_dw.celery import app
from spreadsheet.scripts import SPREADSHEET_SCRIPTS
from spreadsheet.models import Spreadsheet

@app.task
def task_process(spreadsheet_id):
    print(f"Started at {datetime.now()}")
    spreadsheet_model = Spreadsheet.objects.get(pk=spreadsheet_id)
    try:
        processing_rfb = SPREADSHEET_SCRIPTS[spreadsheet_model.processor](spreadsheet_model.spreadsheet)
    except KeyError:
        spreadsheet_model.errors = {"erro": f"Processador {spreadsheet_model.processor} não encontrdo"}
        spreadsheet_model.status = 2
        spreadsheet_model.save()
        print(f"Error at {datetime.now()} Error: Processador {spreadsheet_model.processor} não encontrdo")
        return

    if processing_rfb.is_valid():
        processing_rfb.save()
        spreadsheet_model.status = 3
    else:
        spreadsheet_model.status = 2
        spreadsheet_model.errors = processing_rfb.errors

    spreadsheet_model.save()
    print(f"Finished at {datetime.now()}")