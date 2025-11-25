from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['titulo', 'tipo', 'conteudo', 'imagem', 'ativo', 'destaque']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Título do material'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'conteudo': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Conteúdo do material',
                'rows': 8
            }),
            'imagem': forms.FileInput(attrs={
                'class': 'form-file',
                'accept': 'image/*'
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
            'destaque': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }
        labels = {
            'titulo': 'Título',
            'tipo': 'Tipo de Material',
            'conteudo': 'Conteúdo',
            'imagem': 'Imagem (opcional)',
            'ativo': 'Publicar imediatamente',
            'destaque': 'Marcar como destaque',
        }