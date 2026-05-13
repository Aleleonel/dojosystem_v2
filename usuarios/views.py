from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from accounts.models import User


@login_required
def lista_usuarios(request):

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