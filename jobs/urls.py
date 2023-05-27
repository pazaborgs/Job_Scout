from django.urls import path

from .views import nova_tarefa, nova_vaga, realizar_tarefa, vaga_unica

urlpatterns = [
    path('nova_vaga', nova_vaga, name='nova_vaga'),
    path('vaga_unica/<int:id>', vaga_unica, name='vaga_unica'),
    path('nova_tarefa/<int:id_vaga>', nova_tarefa, name='nova_tarefa'),
    path('realizar_tarefa/<int:id>', realizar_tarefa, name='realizar_tarefa'),
]