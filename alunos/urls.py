from django.urls import path

from .views import (
    lista_alunos,
    criar_aluno,
    editar_aluno,
    excluir_aluno
)

urlpatterns = [

    path(
        '',
        lista_alunos,
        name='lista_alunos'
    ),

    path(
        'novo/',
        criar_aluno,
        name='criar_aluno'
    ),

    path(
        'editar/<int:pk>/',
        editar_aluno,
        name='editar_aluno'
    ),

    path(
        'excluir/<int:pk>/',
        excluir_aluno,
        name='excluir_aluno'
    ),

]