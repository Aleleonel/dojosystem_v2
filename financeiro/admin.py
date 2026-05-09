from django.contrib import admin

from .models import Mensalidade


@admin.register(Mensalidade)
class MensalidadeAdmin(admin.ModelAdmin):

    list_display = (
        'aluno',
        'referencia',
        'valor',
        'status',
        'data_vencimento',
        'academia'
    )

    list_filter = (
        'status',
        'academia',
    )

    search_fields = (
        'aluno__nome',
        'referencia',
    )