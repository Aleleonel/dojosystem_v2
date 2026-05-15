from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from accounts.models import User

from .forms import (
    UsuarioForm,
    UsuarioUpdateForm
)

from permissions.decorators import (
    master_required,
    admin_required
)


@login_required
@admin_required
def lista_usuarios(request):

    # PROFESSOR não acessa usuários
    usuarios = User.objects.filter(
        academia=request.user.academia
    )

    context = {
        'usuarios': usuarios
    }

    return render(
        request,
        'usuarios/lista.html',
        context
    )

@login_required
@admin_required
def criar_usuario(request):

    # PROFESSOR bloqueado

    form = UsuarioForm(
    request.POST or None,
    request.FILES or None
)

    if form.is_valid():

        usuario = form.save(commit=False)

        # força academia do usuário logado

        usuario.academia = request.user.academia

        usuario.save()

        return redirect('lista_usuarios')

    context = {
        'form': form
    }

    return render(
        request,
        'usuarios/form.html',
        context
    )


@login_required
def meu_perfil(request):

    form = UsuarioUpdateForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user
    )

    if form.is_valid():

        form.save()

        return redirect('dashboard')

    context = {
        'form': form
    }

    return render(
        request,
        'usuarios/meu_perfil.html',
        context
    )


@login_required
@admin_required
def editar_usuario(request, pk):

    usuario = get_object_or_404(
        User,
        pk=pk,
        academia=request.user.academia
    )

    # ADMIN não pode editar MASTER

    if (
        request.user.tipo_usuario == 'ADMIN'
        and usuario.tipo_usuario == 'MASTER'
    ):
        return redirect('lista_usuarios')

    form = UsuarioUpdateForm(
        request.POST or None,
        request.FILES or None,
        instance=usuario
    )

    if request.user.tipo_usuario == 'ADMIN':

        form.fields['tipo_usuario'].choices = [
            ('PROFESSOR', 'Professor')
        ]

    if form.is_valid():

        form.save()

        return redirect('lista_usuarios')

    context = {
        'form': form
    }

    return render(
        request,
        'usuarios/form.html',
        context
    )

@login_required
@master_required
def excluir_usuario(request, pk):

    if request.user.tipo_usuario != 'MASTER':
        return redirect('dashboard')

    usuario = get_object_or_404(
        User,
        pk=pk,
        academia=request.user.academia
    )
    # impede excluir a si mesmo

    if usuario == request.user:
        return redirect('lista_usuarios')

    usuario.delete()

    return redirect('lista_usuarios')