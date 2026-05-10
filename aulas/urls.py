from django.urls import path

from .views import (
    lista_aulas,
    criar_aula,
    chamada_aula,
    qr_checkin,
    registrar_presenca_qr
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

    path(
        'checkin/',
        qr_checkin,
        name='qr_checkin'
    ),

    path(
        'registrar-presenca/',
        registrar_presenca_qr,
        name='registrar_presenca_qr'
    ),

]