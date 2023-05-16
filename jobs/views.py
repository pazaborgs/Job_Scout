from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import get_object_or_404, redirect, render

from empresas.forms import CadastroVaga
from empresas.models import Jobs


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

def vaga_unica(request, id):
    vaga_unica = get_object_or_404(Jobs,id = id)
    return render(request, 'jobs/vaga.html', {'vaga': vaga_unica})
