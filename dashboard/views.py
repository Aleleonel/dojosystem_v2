from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.utils.timezone import now

from alunos.models import Aluno
from aulas.models import Presenca
from financeiro.models import Mensalidade


@login_required
def dashboard(request):

    academia = request.user.academia

    total_alunos = Aluno.objects.filter(
        academia=academia
    ).count()

    alunos_ativos = Aluno.objects.filter(
        academia=academia,
        status='ATIVO'
    ).count()

    mensalidades_pendentes = Mensalidade.objects.filter(
        academia=academia,
        status='PENDENTE'
    ).count()

    mensalidades_atrasadas = Mensalidade.objects.filter(
        academia=academia,
        status='PENDENTE',
        data_vencimento__lt=now().date()
    ).count()

    presencas_hoje = Presenca.objects.filter(
        aula__academia=academia,
        aula__data=now().date()
    ).count()

    aniversariantes = Aluno.objects.filter(
        academia=academia,
        data_nascimento__month=now().month
    )

    context = {
        'total_alunos': total_alunos,
        'alunos_ativos': alunos_ativos,
        'mensalidades_pendentes': mensalidades_pendentes,
        'presencas_hoje': presencas_hoje,
        'aniversariantes': aniversariantes,
        'mensalidades_atrasadas': mensalidades_atrasadas,
    }

   
    return render(
        request,
        'dashboard/dashboard.html',
        context
    )

