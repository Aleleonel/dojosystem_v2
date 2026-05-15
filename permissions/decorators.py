from functools import wraps

from django.shortcuts import redirect


def master_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.tipo_usuario != 'MASTER':
            return redirect('dashboard')

        return view_func(request, *args, **kwargs)

    return wrapper


def admin_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.tipo_usuario not in ['MASTER', 'ADMIN']:
            return redirect('dashboard')

        return view_func(request, *args, **kwargs)

    return wrapper


def professor_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.tipo_usuario not in [
            'MASTER',
            'ADMIN',
            'PROFESSOR'
        ]:
            return redirect('dashboard')

        return view_func(request, *args, **kwargs)

    return wrapper