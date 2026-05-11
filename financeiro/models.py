from django.db import models
from academias.models import Academia
from alunos.models import Aluno
from django.utils.timezone import now
from datetime import timedelta


class Mensalidade(models.Model):

    STATUS_CHOICES = (

        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
        ('ATRASADO', 'Atrasado'),

    )

    academia = models.ForeignKey(
        Academia,
        on_delete=models.CASCADE
    )

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    referencia = models.CharField(
        max_length=20
    )

    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    vencimento = models.DateField()

    data_pagamento = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDENTE'
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def atualizar_status(self):

        if (
            self.status == 'PENDENTE'
            and self.vencimento < now().date()
        ):

            self.status = 'ATRASADO'

            self.save()

    def __str__(self):

        return f'{self.aluno.nome} - {self.referencia}'