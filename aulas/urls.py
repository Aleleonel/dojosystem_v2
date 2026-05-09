from django.urls import path

from .views import (
    lista_aulas,
    criar_aula,
    chamada_aula
)

urlpatterns = [

    path(
        '',
        lista_aulas,
        name='lista_aulas'
    ),

    path(
        'nova/',
        criar_aula,
        name='criar_aula'
    ),

    path(
        'chamada/<int:pk>/',
        chamada_aula,
        name='chamada_aula'
    ),

]