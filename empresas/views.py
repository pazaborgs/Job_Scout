from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render

from .models import Company, Specializations, Technologies


def nova_empresa(request):

    if request.method ==  'GET':
        techs = Technologies.objects.all()
        specs = Specializations.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs, 'specs': specs})

    elif request.method == 'POST':
        logo = request.FILES.get('logo')
        name = request.POST.get('name')
        email = request.POST.get('email')
        headquarters = request.POST.get('headquarters')
        technologies = request.POST.getlist('technologies')
        marketing_niche = request.POST.get('marketing_niche')
        specializations = request.POST.getlist('specializations')

        if (len(name.strip()) == 0 or len(email.strip()) == 0 or len(headquarters.strip()) == 0 or len(marketing_niche.strip()) == 0 or (not logo)): 
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/home/nova_empresa')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'A logo da empresa deve ter menos de 10MB')
            return redirect('/home/nova_empresa')

        if marketing_niche not in [i[0] for i in Company.choices_niche]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect('/home/nova_empresa')

        company = Company(logo=logo,
                        name=name,
                        email=email,
                        headquarters=headquarters,
                        marketing_niche=marketing_niche)

        company.save()
        company.technologies.add(*technologies)
        company.save()
        company.specializations.add(*specializations)

        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
        return redirect('/home/empresas')