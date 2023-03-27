from django.urls import path

from empresas.views import index

urlpatterns = [
    path('', index)
]