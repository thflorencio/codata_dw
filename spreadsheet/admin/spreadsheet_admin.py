from django.contrib import admin, messages

from spreadsheet.models import Spreadsheet
from spreadsheet.task import task_process


@admin.action(description="Processar Planilhas Selecionadas")
def process_spreadsheet(modeladmin, request, queryset):
    for model in queryset:
        model.status = 1
        model.save()
        task_process.apply_async(args=[], kwargs={"spreadsheet_id": model.pk})


@admin.register(Spreadsheet)
class SpreedSheetsAdmin(admin.ModelAdmin):
    list_display = ("status", "created_at", "updated_at")
    actions = [
        process_spreadsheet,
    ]
