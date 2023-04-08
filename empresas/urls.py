from django.urls import path

from .views import empresas_cadastradas, excluir_empresa, nova_empresa

urlpatterns = [
    path('nova_empresa', nova_empresa, name='nova_empresa'),
    path('empresas_cadastradas', empresas_cadastradas, name='empresas_cadastradas'),
    path('excluir_empresa/<int:id>', excluir_empresa, name='excluir_empresa')
]