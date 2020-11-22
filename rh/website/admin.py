from django.contrib import admin
from .models import  Curriculo, Vagas

class VagasAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'salario']

admin.site.register(Curriculo)
admin.site.register(Vagas, VagasAdmin)