from django.urls import path

from empresas.views import empresas_cadastradas, nova_empresa

urlpatterns = [
    path('nova_empresa', nova_empresa, name="nova_empresa"),
    path('empresas_cadastradas', empresas_cadastradas, name="empresas_cadastradas")
]