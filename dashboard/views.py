from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.utils import timezone

from django.utils.timezone import now
from aulas.models import Aula

from alunos.models import Aluno
from aulas.models import Presenca
from financeiro.models import Mensalidade

from django.db.models import Sum
from django.utils.timezone import now

from django.db.models.functions import ExtractMonth

from django.db.models import Count
import json


@login_required
def dashboard(request):

    academia = request.user.academia

    hoje = now().date()

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
        vencimento__lt=hoje
    ).count()

    presencas_hoje = Presenca.objects.filter(
        aula__academia=academia,
        aula__data=now().date()
    ).count()

    aniversariantes = Aluno.objects.filter(
        academia=academia,
        data_nascimento__month=now().month
    )
    
    ranking_frequencia = Aluno.objects.filter(
        academia=academia
    ).annotate(
        frequencia_total=Count('presencas')
    ).order_by('-frequencia_total')[:5]

    total_aulas = Aula.objects.filter(
    academia=request.user.academia
    ).count()

    presencas_por_mes = (
        Presenca.objects.filter(
        aula__academia=request.user.academia
    )
    .annotate(
       mes=ExtractMonth('data_hora_presenca')
    )
    .values('mes')
    .annotate(total=Count('id'))
    .order_by('mes')
    )

    meses = []
    totais = []

    nomes_meses = {
        1: 'Jan',
        2: 'Fev',
        3: 'Mar',
        4: 'Abr',
        5: 'Mai',
        6: 'Jun',
        7: 'Jul',
        8: 'Ago',
        9: 'Set',
        10: 'Out',
        11: 'Nov',
        12: 'Dez',
    }

    for item in presencas_por_mes:

        meses.append(
            nomes_meses[item['mes']]
        )

        totais.append(
            item['total']
        )

    mes_atual = now().month
    ano_atual = now().year

    mensalidades_pagas = Mensalidade.objects.filter(
        status='PAGO',
        academia=request.user.academia,
        vencimento__month=mes_atual,
        vencimento__year=ano_atual
    )

    faturamento = mensalidades_pagas.aggregate(
        total=Sum('valor')
    )['total'] or 0

    inadimplentes = Mensalidade.objects.filter(
        status='PENDENTE',
        academia=request.user.academia
    ).count()

    context = {
        'total_alunos': total_alunos,
        'alunos_ativos': alunos_ativos,
        'mensalidades_pendentes': mensalidades_pendentes,
        'presencas_hoje': presencas_hoje,
        'aniversariantes': aniversariantes,
        'mensalidades_atrasadas': mensalidades_atrasadas,
        'ranking_frequencia': ranking_frequencia,
        'faturamento': faturamento,
        'inadimplentes': inadimplentes,
        'total_aulas': total_aulas,
        'meses': json.dumps(meses),
        'totais': json.dumps(totais),
    }

   
    return render(
        request,
        'dashboard/dashboard.html',
        context
    )

