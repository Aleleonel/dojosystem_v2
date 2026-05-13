from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Mensalidade
from .forms import MensalidadeForm

from alunos.models import Aluno
from django.contrib import messages
from django.utils.timezone import now
from core.permissions import admin_required



@login_required
@admin_required
def lista_mensalidades(request):

    mensalidades = Mensalidade.objects.filter(
        academia=request.user.academia
    ).order_by('-vencimento')

    context = {
        'mensalidades': mensalidades
    }

    return render(
        request,
        'financeiro/lista.html',
        context
    )


@login_required
@admin_required
def criar_mensalidade(request):

    form = MensalidadeForm(
        request.POST or None
    )

    form.fields['aluno'].queryset = Aluno.objects.filter(
        academia=request.user.academia
    )

    if form.is_valid():

        mensalidade = form.save(commit=False)

        mensalidade.academia = request.user.academia

        mensalidade.save()

        return redirect('lista_mensalidades')

    context = {
        'form': form
    }

    return render(
        request,
        'financeiro/form.html',
        context
    )


@login_required
@admin_required
def editar_mensalidade(request, pk):

    mensalidade = get_object_or_404(
        Mensalidade,
        pk=pk,
        academia=request.user.academia
    )

    form = MensalidadeForm(
        request.POST or None,
        instance=mensalidade
    )

    form.fields['aluno'].queryset = Aluno.objects.filter(
        academia=request.user.academia
    )

    if form.is_valid():

        form.save()

        return redirect('lista_mensalidades')

    context = {
        'form': form
    }

    return render(
        request,
        'financeiro/form.html',
        context
    )


@login_required
@admin_required
def excluir_mensalidade(request, pk):

    mensalidade = get_object_or_404(
        Mensalidade,
        pk=pk,
        academia=request.user.academia
    )

    mensalidade.delete()

    return redirect('lista_mensalidades')


@login_required
@admin_required
def gerar_mensalidades(request):

    hoje = now().date()

    referencia = hoje.strftime('%m/%Y')

    alunos = Aluno.objects.filter(
        academia=request.user.academia,
        status='ATIVO'
    )

    mensalidades_criadas = 0

    for aluno in alunos:

        existe = Mensalidade.objects.filter(
            aluno=aluno,
            referencia=referencia
        ).exists()

        if not existe:

            Mensalidade.objects.create(

                academia=request.user.academia,

                aluno=aluno,

                referencia=referencia,

                valor=150.00,

                vencimento=hoje.replace(day=10),

                status='PENDENTE'

            )

            mensalidades_criadas += 1

    messages.success(
        request,
        f'{mensalidades_criadas} mensalidades geradas.'
    )

    return redirect('lista_mensalidades')