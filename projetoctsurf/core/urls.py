from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    # A URL raiz agora aponta para o dashboard, que é protegido.
    path('', views.dashboard, name='dashboard'),
    
    # A URL de login, usando a view padrão do Django.
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    
    # A URL de logout, com um redirecionamento para a página de login.
    # Quando o usuário faz logout, ele será levado para a tela de login.
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]