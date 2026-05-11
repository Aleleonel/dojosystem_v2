from django.contrib import admin

from .models import Mensalidade


@admin.register(Mensalidade)
class MensalidadeAdmin(admin.ModelAdmin):

    list_display = (
        'aluno',
        'referencia',
        'valor',
        'vencimento',
        'status'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'aluno__nome',
    )