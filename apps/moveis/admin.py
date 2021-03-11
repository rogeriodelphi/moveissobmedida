from django.contrib import admin

from .models import Movel


@admin.register(Movel)
class MovelAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao', 'cor', 'valor', 'situacao', 'categoria']
    display_links = ['nome']
