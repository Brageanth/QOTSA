from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Inscrito

class InscritoAdmin(admin.ModelAdmin):
	model = Inscrito
	list_display = ('nombre', 'apellido', 'correo', 'celular', 'codigo')
	search_fields = ('nombre', 'apellido', 'correo', 'celular', 'codigo')

admin.site.register(Inscrito, InscritoAdmin)