from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "cargo", "email", "idade", "cpf")
    search_fields = ("nome", "email", "cpf")
    list_filter = ("cargo", "idade")
