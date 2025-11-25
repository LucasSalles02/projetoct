from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'data_publicacao', 'ativo', 'destaque']
    list_filter = ['tipo', 'ativo', 'destaque']
    search_fields = ['titulo', 'conteudo']
    date_hierarchy = 'data_publicacao'