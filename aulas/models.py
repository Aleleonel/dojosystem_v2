from django.db import models

from academias.models import Academia
from accounts.models import User
from alunos.models import Aluno


class Aula(models.Model):

    class Modalidade(models.TextChoices):
        JIU_JITSU = 'JIU_JITSU', 'Jiu-Jitsu'
        NO_GI = 'NO_GI', 'No-Gi'
        INFANTIL = 'INFANTIL', 'Infantil'
        FEMININO = 'FEMININO', 'Feminino'

    academia = models.ForeignKey(
        Academia,
        on_delete=models.CASCADE,
        related_name='aulas'
    )

    professor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='aulas'
    )

    modalidade = models.CharField(
        max_length=30,
        choices=Modalidade.choices
    )

    data = models.DateField()

    horario_inicio = models.TimeField()

    horario_fim = models.TimeField()

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    criada_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.modalidade} - {self.data}'


class Presenca(models.Model):

    aula = models.ForeignKey(
        Aula,
        on_delete=models.CASCADE,
        related_name='presencas'
    )

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='presencas'
    )

    data_hora_presenca = models.DateTimeField(
        auto_now_add=True
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ('aula', 'aluno')

    def __str__(self):
        return f'{self.aluno.nome} - {self.aula}'