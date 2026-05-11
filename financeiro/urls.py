from django.urls import path

from .views import (
    lista_mensalidades,
    criar_mensalidade,
    editar_mensalidade,
    excluir_mensalidade,
    gerar_mensalidades
)

urlpatterns = [

    path(
        '',
        lista_mensalidades,
        name='lista_mensalidades'
    ),

    path(
        'nova/',
        criar_mensalidade,
        name='criar_mensalidade'
    ),

    path(
        'editar/<int:pk>/',
        editar_mensalidade,
        name='editar_mensalidade'
    ),

    path(
        'excluir/<int:pk>/',
        excluir_mensalidade,
        name='excluir_mensalidade'
    ),

    path(
        'gerar/',
        gerar_mensalidades,
        name='gerar_mensalidades'
    ),

]