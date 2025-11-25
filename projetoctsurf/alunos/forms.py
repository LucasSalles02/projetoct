from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'data_nascimento', 
                  'endereco', 'bairro', 'cidade', 'cep',
                  'nome_responsavel', 'cpf_responsavel', 'numero_responsavel',
                  'turma', 'situacao', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nome completo do aluno'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '00000000000',
                'maxlength': '11'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Rua, número'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Bairro'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Cidade'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '00000-000',
                'maxlength': '9'
            }),
            'nome_responsavel': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nome completo do responsável'
            }),
            'cpf_responsavel': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '00000000000',
                'maxlength': '11'
            }),
            'numero_responsavel': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '00000000000',
                'maxlength': '11'
            }),
            'turma': forms.Select(attrs={
                'class': 'form-select'
            }),
            'situacao': forms.Select(attrs={
                'class': 'form-select'
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Observações adicionais (opcional)',
                'rows': 4
            }),
        }