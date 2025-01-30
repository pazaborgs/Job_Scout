from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import get_object_or_404, redirect, render

from empresas.forms import CadastroVaga
from empresas.models import Jobs

from .models import Task


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
            return redirect(f'/home/empresa_unica/{company_id}')

def vaga_unica(request, id):
    vaga_unica = get_object_or_404(Jobs,id = id)
    tarefas = Task.objects.filter(job_id = vaga_unica)
    return render(request, 'jobs/vaga.html', {'vaga': vaga_unica, 'tarefas': tarefas})

 
def nova_tarefa(request, id_vaga): # Precisa adicionar validação de

    title = request.POST.get('title')
    priority = request.POST.get("priority")
    date = request.POST.get('date')
    
    tarefa = Task(job_id=id_vaga,
                    title=title,
                    priority=priority,
                    date=date)
    tarefa.save()
    messages.add_message(request, constants.SUCCESS, 'Tarefa criada com sucesso')
    return redirect(f'/jobs/vaga_unica/{id_vaga}')

def realizar_tarefa(request, id):

    task = Task.objects.filter(id=id).filter(finished=False).first()

    if not task:

        messages.add_message(request, constants.ERROR, 'Erro interno do sistema ou tarefa não encontrada!')
        return redirect('/home/empresas/')

    else:
        task.delete()
        messages.add_message(request, constants.SUCCESS, 'Tarefa deletada com sucesso!')
        return redirect(f'/jobs/vaga_unica/{task.job.id}')



