from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render

from empresas.forms import CadastroEmpresa

from .models import Company, Specializations, Technologies


def nova_empresa(request):

    if request.method ==  'GET':
        form = CadastroEmpresa()
        return render(request, 'nova_empresa.html', {'form': form})

    elif request.method == 'POST':

        form = CadastroEmpresa(request.POST, request.FILES)
    
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
            return redirect('/home/nova_empresa')
       
        else:
            messages.add_message(request, constants.ERROR, 'Empresa não cadastrada')
            return render(request, 'nova_empresa.html', {'form': form})

def empresas_cadastradas(request):

    companies = Company.objects.all()
    technologies = Technologies.objects.all()
    specializations = Specializations.objects.all()
    return render(request, 'empresas_cadastradas.html', {'companies': companies, 'technologies': technologies, 'specializations': specializations})

def excluir_empresa(request, id):
    company = Company.objects.get(id = id)
    company.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa excluída com sucesso')
    return redirect('/home/empresas_cadastradas')