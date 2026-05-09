from django.contrib import admin

from .models import Graduacao, Aluno


@admin.register(Graduacao)
class GraduacaoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'graus',
        'ordem',
        'academia'
    )

    search_fields = (
        'nome',
    )


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'graduacao',
        'telefone',
        'status',
        'academia'
    )

    search_fields = (
        'nome',
        'telefone',
    )

    list_filter = (
        'status',
        'graduacao',
        'academia'
    )