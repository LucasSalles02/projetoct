from django.db import models
from django.utils import timezone

class Material(models.Model):
    TIPO_CHOICES = [
        ('noticia', 'Notícia'),
        ('evento', 'Evento'),
        ('dica', 'Dica de Surf'),
        ('galeria', 'Galeria'),
    ]
    
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='noticia')
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='materiais/', blank=True, null=True)
    data_publicacao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'
        ordering = ['-data_publicacao']
    
    def __str__(self):
        return self.titulo