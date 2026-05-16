from alunos.models import Aluno
from accounts.models import User
from aulas.models import Aula
from financeiro.models import Mensalidade


def alunos_da_academia(request):

    return Aluno.objects.filter(
        academia=request.user.academia
    )


def usuarios_da_academia(request):

    return User.objects.filter(
        academia=request.user.academia
    )


def aulas_da_academia(request):

    return Aula.objects.filter(
        academia=request.user.academia
    )


def mensalidades_da_academia(request):

    return Mensalidade.objects.filter(
        academia=request.user.academia
    )