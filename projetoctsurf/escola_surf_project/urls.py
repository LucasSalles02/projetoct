from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('alunos/', include('alunos.urls')),
    path('turmas/', include('turmas.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('materiais/', include('materiais.urls')),
    path('equipamentos/', include('equipamentos.urls')),
]

# Servir arquivos de media e static durante desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)