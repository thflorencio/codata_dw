from django.contrib import admin, messages

from cnpj.models import Spreedsheets
@admin.action(description='Processar Planilhas Selecionadas')
def process_spreedsheet(modeladmin, request, queryset):
    for model in queryset:
        model.process()

@admin.register(Spreedsheets)
class SpreedSheetsAdmin(admin.ModelAdmin):
    list_display = ('status', 'created_at', 'updated_at')
    actions = [process_spreedsheet, ]
