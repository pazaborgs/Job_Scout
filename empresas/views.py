from django.http import HttpResponse
from django.shortcuts import render

from .models import Specializations, Technologies


def index(request):
    techs = Technologies.objects.all()
    specs = Specializations.objects.all()
    return render(request, "empresas.html", {'techs': techs})
