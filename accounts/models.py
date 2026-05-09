from django.db import models
from django.contrib.auth.models import AbstractUser

from academias.models import Academia


class User(AbstractUser):

    class TipoUsuario(models.TextChoices):
        MASTER = 'MASTER', 'Master'
        ADMIN = 'ADMIN', 'Administrador'
        PROFESSOR = 'PROFESSOR', 'Professor'

    academia = models.ForeignKey(
        Academia,
        on_delete=models.CASCADE,
        related_name='usuarios',
        null=True,
        blank=True
    )

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.PROFESSOR
    )

    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    foto = models.ImageField(
        upload_to='usuarios/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username