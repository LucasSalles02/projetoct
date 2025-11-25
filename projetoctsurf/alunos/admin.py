from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "data_nascimento",
        "cpf",
        "cidade",
        "nome_responsavel",
        "numero_responsavel",
    )
    search_fields = ("nome", "cpf", "nome_responsavel", "cpf_responsavel")
    
    
    list_filter = ("cidade",) 
    
    ordering = ("nome",)
    list_per_page = 20