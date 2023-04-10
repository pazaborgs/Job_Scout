from django.urls import path

from .views import nova_vaga

urlpatterns = [
    path('nova_vaga', nova_vaga, name="nova_vaga")
]