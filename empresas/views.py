from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import get_object_or_404, redirect, render

from empresas.forms import CadastroEmpresa, CadastroVaga

from .models import Company, Jobs, Technologies


def nova_empresa(request):

    if request.method ==  'GET':
        form = CadastroEmpresa()
        return render(request, 'nova_empresa.html', {'form': form})

    elif request.method == 'POST':

        form = CadastroEmpresa(request.POST, request.FILES)
        print('FUCK')
    
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
            return redirect('/home/nova_empresa')
       
        else:
            messages.add_message(request, constants.ERROR, 'Empresa não cadastrada')
            return render(request, 'nova_empresa.html', {'form': form})

def empresas_cadastradas(request):

    name_filter = request.GET.get('name')
    techs_filter = request.GET.get('technologies')
    companies = Company.objects.all()

    if name_filter:
        companies = companies.filter(name__icontains = name_filter)

    if techs_filter:
        companies = companies.filter(technologies = techs_filter)
    
    techs = Technologies.objects.all()
    return render(request, 'empresas_cadastradas.html', {'companies': companies, 'techs': techs})


def empresa_unica(request, id):
    form = CadastroVaga()
    unique_company = get_object_or_404(Company, id=id)
    jobs = Jobs.objects.filter(company_id = id)
    return render(request, 'empresa_unica.html', {'company': unique_company, 'form':form, 'jobs':jobs}) 
    

def excluir_empresa(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa excluída com sucesso')
    return redirect('/home/empresas_cadastradas')