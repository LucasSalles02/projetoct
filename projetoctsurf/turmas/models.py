from django.db import models
from funcionarios.models import Funcionario

class Turma(models.Model):
    NIVEIS = [
        ("iniciante", "Iniciante"),
        ("intermediario", "Intermediário"),
        ("avancado", "Avançado"),
    ]

    nome = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVEIS)  
    quantidade_alunos = models.PositiveIntegerField(default=0)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    professor = models.ForeignKey(
        Funcionario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'cargo': 'instrutor'},
        related_name="turmas"
    )

    def __str__(self):
        return f"{self.nome} ({self.get_nivel_display()})"
