from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Material
from .forms import MaterialForm

def acesso_publico(request):
    """View pública - listagem de materiais"""
    materiais = Material.objects.filter(ativo=True)
    destaques = materiais.filter(destaque=True)[:3]
    
    # Filtro por tipo (opcional)
    tipo_filtro = request.GET.get('tipo')
    if tipo_filtro:
        materiais = materiais.filter(tipo=tipo_filtro)
    
    context = {
        'materiais': materiais,
        'destaques': destaques,
        'titulo': 'Acesso Público'
    }
    return render(request, 'materiais/acesso_publico.html', context)

def detalhe_material(request, pk):
    """View pública - detalhe de um material"""
    material = get_object_or_404(Material, pk=pk, ativo=True)
    
    context = {
        'material': material,
        'titulo': material.titulo
    }
    return render(request, 'materiais/detalhe_material.html', context)

def lista_materiais_admin(request):
    """View administrativa - gerenciar materiais"""
    materiais = Material.objects.all().order_by('-data_publicacao')
    
    context = {
        'materiais': materiais,
        'titulo': 'Gerenciar Materiais'
    }
    return render(request, 'materiais/lista_materiais_admin.html', context)

def cadastro_material(request):
    """View administrativa - cadastrar novo material"""
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material publicado com sucesso!')
            return redirect('materiais:lista_materiais_admin')
    else:
        form = MaterialForm()
    
    context = {
        'form': form,
        'titulo': 'Publicar Material'
    }
    return render(request, 'materiais/cadastro_material.html', context)

def editar_material(request, pk):
    """View administrativa - editar material"""
    material = get_object_or_404(Material, pk=pk)
    
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material atualizado com sucesso!')
            return redirect('materiais:lista_materiais_admin')
    else:
        form = MaterialForm(instance=material)
    
    context = {
        'form': form,
        'material': material,
        'titulo': 'Editar Material'
    }
    return render(request, 'materiais/cadastro_material.html', context)

def deletar_material(request, pk):
    """View administrativa - deletar material"""
    material = get_object_or_404(Material, pk=pk)
    material.delete()
    messages.success(request, 'Material excluído com sucesso!')
    return redirect('materiais:lista_materiais_admin')