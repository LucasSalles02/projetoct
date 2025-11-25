from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# View para a página inicial, que qualquer usuário pode ver
def home(request):
    # Se o usuário já estiver autenticado, redireciona para o dashboard
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    return render(request, 'core/home.html')

# View para o dashboard, que só é acessível após o login
@login_required
def dashboard(request):
    context = {
        'user': request.user,
    }
    return render(request, 'core/dashboard.html', context)