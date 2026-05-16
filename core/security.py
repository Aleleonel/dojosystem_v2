from django.shortcuts import get_object_or_404

from accounts.models import User
from alunos.models import Aluno
from aulas.models import Aula
from financeiro.models import Mensalidade


def get_usuario_da_academia(request, pk):

    return get_object_or_404(
        User,
        pk=pk,
        academia=request.user.academia
    )


def get_aluno_da_academia(request, pk):

    return get_object_or_404(
        Aluno,
        pk=pk,
        academia=request.user.academia
    )


def get_aula_da_academia(request, pk):

    return get_object_or_404(
        Aula,
        pk=pk,
        academia=request.user.academia
    )


def get_mensalidade_da_academia(request, pk):

    return get_object_or_404(
        Mensalidade,
        pk=pk,
        academia=request.user.academia
    )