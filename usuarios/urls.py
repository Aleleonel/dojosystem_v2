from django.urls import path

from .views import (
    lista_usuarios,
    criar_usuario,
    editar_usuario,
    excluir_usuario,
)

urlpatterns = [

    path(
        '',
        lista_usuarios,
        name='lista_usuarios'
    ),

    path(
        'novo/',
        criar_usuario,
        name='criar_usuario'
    ),

    path(
        'editar/<int:pk>/',
        editar_usuario,
        name='editar_usuario'
    ),

    path(
        'excluir/<int:pk>/',
        excluir_usuario,
        name='excluir_usuario'
    ),

]