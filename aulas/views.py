from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Aula
from .models import Presenca

from .forms import AulaForm

from alunos.models import Aluno

from accounts.models import User

from django.http import JsonResponse


@login_required
def lista_aulas(request):

    aulas = Aula.objects.filter(
        academia=request.user.academia
    ).order_by('-data')

    context = {
        'aulas': aulas
    }

    return render(
        request,
        'aulas/lista.html',
        context
    )


@login_required
def criar_aula(request):

    form = AulaForm(
        request.POST or None
    )

    form.fields['professor'].queryset = User.objects.filter(
        academia=request.user.academia
    )

    if form.is_valid():

        aula = form.save(commit=False)

        aula.academia = request.user.academia

        aula.save()

        return redirect('lista_aulas')

    context = {
        'form': form
    }

    return render(
        request,
        'aulas/form.html',
        context
    )


@login_required
def chamada_aula(request, pk):

    aula = get_object_or_404(
        Aula,
        pk=pk,
        academia=request.user.academia
    )

    alunos = Aluno.objects.filter(
        academia=request.user.academia,
        status='ATIVO'
    )

    if request.method == 'POST':

        alunos_ids = request.POST.getlist('alunos')

        for aluno_id in alunos_ids:

            aluno = Aluno.objects.get(id=aluno_id)

            Presenca.objects.get_or_create(
                aula=aula,
                aluno=aluno
            )

        return redirect('lista_aulas')

    context = {
        'aula': aula,
        'alunos': alunos
    }


    return render(
        request,
        'aulas/chamada.html',
        context
    )


@login_required
def qr_checkin(request):

    return render(
        request,
        'aulas/checkin.html'
    )


@login_required
def registrar_presenca_qr(request):

    if request.method == 'POST':

        codigo = request.POST.get('codigo')

        try:

            aluno_id = codigo.split(':')[1]

            aluno = Aluno.objects.get(
                id=aluno_id,
                academia=request.user.academia
            )

            aula = Aula.objects.filter(
                academia=request.user.academia
            ).last()

            if not aula:

                return JsonResponse({
                    'success': False,
                    'message': 'Nenhuma aula encontrada.'
                })

            Presenca.objects.get_or_create(
                aula=aula,
                aluno=aluno
            )

            return JsonResponse({
                'success': True,
                'message': f'{aluno.nome} registrado com sucesso!'
            })

        except:

            return JsonResponse({
                'success': False,
                'message': 'QR Code inválido.'
            })