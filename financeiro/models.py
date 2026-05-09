from django.db import models

from academias.models import Academia
from alunos.models import Aluno


class Mensalidade(models.Model):

    class StatusPagamento(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        PAGO = 'PAGO', 'Pago'
        ATRASADO = 'ATRASADO', 'Atrasado'
        CANCELADO = 'CANCELADO', 'Cancelado'

    academia = models.ForeignKey(
        Academia,
        on_delete=models.CASCADE,
        related_name='mensalidades'
    )

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='mensalidades'
    )

    referencia = models.CharField(
        max_length=20
    )

    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    desconto = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    valor_pago = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    data_vencimento = models.DateField()

    data_pagamento = models.DateField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=StatusPagamento.choices,
        default=StatusPagamento.PENDENTE
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    criada_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.aluno.nome} - {self.referencia}'