from django.urls import path
from . import views

app_name = 'materiais'

urlpatterns = [
    # Área pública
    path('', views.acesso_publico, name='acesso_publico'),
    path('material/<int:pk>/', views.detalhe_material, name='detalhe_material'),
    
    # Área administrativa
    path('admin/lista/', views.lista_materiais_admin, name='lista_materiais_admin'),
    path('admin/cadastro/', views.cadastro_material, name='cadastro_material'),
    path('admin/editar/<int:pk>/', views.editar_material, name='editar_material'),
    path('admin/deletar/<int:pk>/', views.deletar_material, name='deletar_material'),
]