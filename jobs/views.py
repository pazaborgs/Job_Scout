from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect

from empresas.forms import CadastroVaga


def nova_vaga(request):
    if request.method == 'POST':
        form = CadastroVaga(request.POST)
        company_id = request.POST.get('company')
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Vaga cadastrada com sucesso')
            return redirect(f'/home/empresa_unica/{company_id}')
        else:
            messages.add_message(request, constants.ERROR, 'Ocorreu um erro')
        
