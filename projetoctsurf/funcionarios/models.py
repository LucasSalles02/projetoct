from django.db import models

class Funcionario(models.Model):
    CARGOS = [
        ("instrutor", "Instrutor"),
        ("recepcao", "Recepção"),
        ("administracao", "Administração"),
    ]

    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=20, choices=CARGOS)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    idade = models.PositiveIntegerField()
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome} ({self.get_cargo_display()})"
