from django.contrib import admin

from .models import Aula, Presenca


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):

    list_display = (
        'modalidade',
        'data',
        'horario_inicio',
        'professor',
        'academia'
    )

    list_filter = (
        'modalidade',
        'academia',
        'data'
    )

    search_fields = (
        'modalidade',
    )


@admin.register(Presenca)
class PresencaAdmin(admin.ModelAdmin):

    list_display = (
        'aluno',
        'aula',
        'data_hora_presenca'
    )

    search_fields = (
        'aluno__nome',
    )

    list_filter = (
        'aula',
    )