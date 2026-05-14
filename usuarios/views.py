from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from accounts.models import User

from .forms import UsuarioForm


@login_required
def lista_usuarios(request):

    # PROFESSOR não acessa usuários

    if request.user.tipo_usuario == 'PROFESSOR':
        return redirect('dashboard')

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
def criar_usuario(request):

    # PROFESSOR bloqueado

    if request.user.tipo_usuario == 'PROFESSOR':
        return redirect('dashboard')

    form = UsuarioForm(
        request.POST or None,
        request.FILES or None,
        usuario_logado=request.user
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
def editar_usuario(request, pk):

    # PROFESSOR bloqueado

    if request.user.tipo_usuario == 'PROFESSOR':
        return redirect('dashboard')

    usuario = get_object_or_404(
        User,
        pk=pk,
        academia=request.user.academia
    )

    form = UsuarioForm(
        request.POST or None,
        request.FILES or None,
        instance=usuario,
        usuario_logado=request.user
    )

    if form.is_valid():

        usuario = form.save(commit=False)

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
def excluir_usuario(request, pk):

    # apenas MASTER pode excluir

    if request.user.tipo_usuario != 'MASTER':
        return redirect('dashboard')

    usuario = get_object_or_404(
        User,
        pk=pk,
        academia=request.user.academia
    )

    # evita excluir a si próprio

    if usuario == request.user:
        return redirect('lista_usuarios')

    usuario.delete()

    return redirect('lista_usuarios')