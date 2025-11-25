from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Aluno
from .forms import AlunoForm

def lista_alunos(request):
    """Lista todos os alunos"""
    alunos = Aluno.objects.all().select_related('turma')
    
    context = {
        'alunos': alunos,
        'titulo': 'Lista de Alunos'
    }
    return render(request, 'alunos/lista_alunos.html', context)

def cadastro_aluno(request):
    """Cadastrar novo aluno"""
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save()
            messages.success(request, f'Aluno {aluno.nome} cadastrado com sucesso!')
            return redirect('alunos:lista_alunos')
    else:
        form = AlunoForm()
    
    context = {
        'form': form,
        'titulo': 'Nova Inscrição'
    }
    return render(request, 'alunos/cadastro_aluno.html', context)

def editar_aluno(request, pk):
    """Editar dados do aluno"""
    aluno = get_object_or_404(Aluno, pk=pk)
    
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dados de {aluno.nome} atualizados com sucesso!')
            return redirect('alunos:lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    
    context = {
        'form': form,
        'aluno': aluno,
        'titulo': f'Editar Aluno: {aluno.nome}'
    }
    return render(request, 'alunos/cadastro_aluno.html', context)

def deletar_aluno(request, pk):
    """Deletar aluno"""
    aluno = get_object_or_404(Aluno, pk=pk)
    nome = aluno.nome
    aluno.delete()
    messages.success(request, f'Aluno {nome} excluído com sucesso!')
    return redirect('alunos:lista_alunos')

def detalhe_aluno(request, pk):
    """Ver detalhes do aluno"""
    aluno = get_object_or_404(Aluno, pk=pk)
    
    context = {
        'aluno': aluno,
        'titulo': f'Detalhes: {aluno.nome}'
    }
    return render(request, 'alunos/detalhe_aluno.html', context)