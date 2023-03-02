from django.contrib import admin, messages

from spreadsheet.models import Spreadsheet
@admin.action(description='Processar Planilhas Selecionadas')
def process_spreadsheet(modeladmin, request, queryset):
    for model in queryset:
        model.process()

@admin.register(Spreadsheet)
class SpreedSheetsAdmin(admin.ModelAdmin):
    list_display = ('status', 'created_at', 'updated_at')
    actions = [process_spreadsheet, ]
