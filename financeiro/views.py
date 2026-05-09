from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Mensalidade
from .forms import MensalidadeForm

from alunos.models import Aluno


@login_required
def lista_mensalidades(request):

    mensalidades = Mensalidade.objects.filter(
        academia=request.user.academia
    ).order_by('-data_vencimento')

    context = {
        'mensalidades': mensalidades
    }

    return render(
        request,
        'financeiro/lista.html',
        context
    )


@login_required
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
def excluir_mensalidade(request, pk):

    mensalidade = get_object_or_404(
        Mensalidade,
        pk=pk,
        academia=request.user.academia
    )

    mensalidade.delete()

    return redirect('lista_mensalidades')