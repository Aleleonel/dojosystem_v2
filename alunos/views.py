from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Aluno
from .forms import AlunoForm

from core.services import alunos_da_academia

from core.security import get_aluno_da_academia

from core.permissions import (
    admin_required,
    professor_or_admin_required
)


@login_required
@professor_or_admin_required
def lista_alunos(request):

    alunos = alunos_da_academia(
        request
    ).order_by('nome')

    context = {
        'alunos': alunos
    }

    return render(
        request,
        'alunos/lista.html',
        context
    )


@login_required
@professor_or_admin_required
def criar_aluno(request):

    form = AlunoForm(
        request.POST or None,
        request.FILES or None,
        academia=request.user.academia
    )

    if form.is_valid():

        aluno = form.save(commit=False)

        aluno.academia = request.user.academia

        aluno.save()

        return redirect('lista_alunos')

    context = {
        'form': form
    }

    return render(
        request,
        'alunos/form.html',
        context
    )


@login_required
@professor_or_admin_required
def editar_aluno(request, pk):

    aluno = get_aluno_da_academia(
        request,
        pk
)

    form = AlunoForm(
        request.POST or None,
        request.FILES or None,
        instance=aluno,
        academia=request.user.academia
    )

    if form.is_valid():
        form.save()
        return redirect('lista_alunos')

    context = {
        'form': form
    }

    return render(
        request,
        'alunos/form.html',
        context
    )


@login_required
@admin_required
def excluir_aluno(request, pk):

    aluno = get_aluno_da_academia(
        request,
        pk
    )
    aluno.delete()

    return redirect('lista_alunos')

