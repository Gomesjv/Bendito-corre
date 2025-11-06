from django.contrib import admin
from tenis.models import tenis

_field_names = [f.name for f in tenis._meta.fields]

class TenisAdmin(admin.ModelAdmin):
    list_display = tuple(_field_names)           
    search_fields = ('model',) if 'model' in _field_names else (_field_names[0],)

admin.site.register(tenis, TenisAdmin)