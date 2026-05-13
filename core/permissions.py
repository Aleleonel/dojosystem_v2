from functools import wraps

from django.shortcuts import redirect
from django.contrib import messages


def admin_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.tipo_usuario not in ['MASTER', 'ADMIN']:

            messages.error(
                request,
                'Você não possui permissão para acessar esta área.'
            )

            return redirect('dashboard')

        return view_func(request, *args, **kwargs)

    return wrapper


def professor_or_admin_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.tipo_usuario not in [
            'MASTER',
            'ADMIN',
            'PROFESSOR'
        ]:

            messages.error(
                request,
                'Você não possui permissão para acessar esta área.'
            )

            return redirect('dashboard')

        return view_func(request, *args, **kwargs)

    return wrapper


def master_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.tipo_usuario != 'MASTER':

            messages.error(
                request,
                'Acesso permitido apenas para MASTER.'
            )

            return redirect('dashboard')

        return view_func(request, *args, **kwargs)

    return wrapper