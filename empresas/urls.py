from django.urls import path

from empresas.views import index

urlpatterns = [
    path('nova_empresa', index, name="nova_empresa")
]