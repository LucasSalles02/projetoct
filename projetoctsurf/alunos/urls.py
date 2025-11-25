from django.urls import path
from . import views

app_name = 'alunos'

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('cadastro/', views.cadastro_aluno, name='cadastro_aluno'),
    path('editar/<int:pk>/', views.editar_aluno, name='editar_aluno'),
    path('deletar/<int:pk>/', views.deletar_aluno, name='deletar_aluno'),
    path('detalhe/<int:pk>/', views.detalhe_aluno, name='detalhe_aluno'),
]