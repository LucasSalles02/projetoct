from django.contrib import admin
from .models import Turma

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nivel", "data_inicio", "data_fim", "professor", "quantidade_alunos")
    search_fields = ("nome",)
    list_filter = ("nivel", "data_inicio")
