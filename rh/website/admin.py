from django.contrib import admin
from .models import  Resumo, Position

class PositionAdmin(admin.ModelAdmin):
    list_display = ['title', 'salary']

admin.site.register(Resumo)
admin.site.register(Position, PositionAdmin)