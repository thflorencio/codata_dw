from django.contrib import admin


from cnpj.models import CnpjCei

@admin.register(CnpjCei)
class CnpjCeiAdmin(admin.ModelAdmin):

    list_display = ('identification_number', 'name', 'registration_status')

    search_fields = (
        "identification_number", 'name',
    )
