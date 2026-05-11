from django.db import models

from academias.models import Academia

import qrcode

from io import BytesIO

from django.core.files import File

from PIL import Image


class Graduacao(models.Model):

    class CorFaixa(models.TextChoices):
        BRANCA = 'BRANCA', 'Branca'
        CINZA = 'CINZA', 'Cinza'
        AMARELA = 'AMARELA', 'Amarela'
        LARANJA = 'LARANJA', 'Laranja'
        VERDE = 'VERDE', 'Verde'
        AZUL = 'AZUL', 'Azul'
        ROXA = 'ROXA', 'Roxa'
        MARROM = 'MARROM', 'Marrom'
        PRETA = 'PRETA', 'Preta'

    academia = models.ForeignKey(
        Academia,
        on_delete=models.CASCADE,
        related_name='graduacoes'
    )

    nome = models.CharField(
        max_length=30,
        choices=CorFaixa.choices
    )

    graus = models.PositiveIntegerField(default=0)

    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.nome}'
    


class Aluno(models.Model):

    class StatusAluno(models.TextChoices):
        ATIVO = 'ATIVO', 'Ativo'
        INATIVO = 'INATIVO', 'Inativo'
        TRANCADO = 'TRANCADO', 'Trancado'

    academia = models.ForeignKey(
        Academia,
        on_delete=models.CASCADE,
        related_name='alunos'
    )

    qr_code = models.ImageField(
        upload_to='qrcodes/',
        blank=True,
        null=True
    )

    graduacao = models.ForeignKey(
        Graduacao,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='alunos'
    )

    nome = models.CharField(max_length=150)

    foto = models.ImageField(
        upload_to='alunos/',
        blank=True,
        null=True
    )

    data_nascimento = models.DateField()

    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    altura = models.DecimalField(
    max_digits=5,
    decimal_places=2,
    null=True,
    blank=True
)

    tempo_graduacao = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=StatusAluno.choices,
        default=StatusAluno.ATIVO
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome
    
    @property
    def total_presencas(self):

        from aulas.models import Presenca

        return Presenca.objects.filter(
            aluno=self
        ).count()

    @property
    def total_presencas(self):

        from aulas.models import Presenca

        return Presenca.objects.filter(
            aluno=self
        ).count()

    @property
    def total_aulas(self):

        from aulas.models import Aula

        return Aula.objects.filter(
            academia=self.academia
        ).count()

    @property
    def percentual_frequencia(self):

        if self.total_aulas == 0:
            return 0

        percentual = (
            self.total_presencas
            / self.total_aulas
        ) * 100

        return round(percentual, 1)
    

    def save(self, *args, **kwargs):
        

        super().save(*args, **kwargs)

        qr_image = qrcode.make(
            f'aluno:{self.id}'
        )

        buffer = BytesIO()

        qr_image.save(
            buffer,
            format='PNG'
        )

        file_name = f'aluno_{self.id}.png'

        self.qr_code.save(
            file_name,
            File(buffer),
            save=False
        )

        super().save(*args, **kwargs)