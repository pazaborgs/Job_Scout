from django.urls import path

from .views import nova_vaga, vaga_unica

urlpatterns = [
    path('nova_vaga', nova_vaga, name='nova_vaga'),
    path('vaga_unica/<int:id>', vaga_unica, name='vaga_unica')
]