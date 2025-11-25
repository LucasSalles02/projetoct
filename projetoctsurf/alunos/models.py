from django.db import models
from django.utils import timezone

class Aluno(models.Model):
    SITUACAO_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('pendente', 'Pendente'),
    ]
    
    # Campos PRINCIPAIS
    nome = models.CharField(max_length=100, verbose_name='Nome Completo')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    
    # Campos de Endereço
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    cep = models.CharField(max_length=9, verbose_name='CEP')

    # Campos de Responsável
    nome_responsavel = models.CharField(max_length=100, verbose_name='Nome do Responsável')
    cpf_responsavel = models.CharField(max_length=11, verbose_name='CPF do Responsável')
    numero_responsavel = models.CharField(max_length=11, verbose_name='Telefone do Responsável')
    
    # Campos adicionais
    turma = models.ForeignKey(
        'turmas.Turma', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='alunos',
        verbose_name='Turma'
    )
    
    situacao = models.CharField(
        max_length=20, 
        choices=SITUACAO_CHOICES, 
        default='ativo',
        verbose_name='Situação'
    )
    
    data_inscricao = models.DateTimeField(default=timezone.now, verbose_name='Data de Inscrição')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['-data_inscricao']
    
    def __str__(self):
        return self.nome