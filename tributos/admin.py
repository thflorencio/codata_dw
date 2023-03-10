from django.contrib import admin


from tributos.models import Iss

@admin.register(Iss)
class IssAdmin(admin.ModelAdmin):
    list_display = ("identification_number", "base_calculo", "iss_value", "period")
