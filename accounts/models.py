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
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='usuarios'
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

    @property
    def is_master(self):
        return self.tipo_usuario == 'MASTER'

    @property
    def is_admin(self):
        return self.tipo_usuario == 'ADMIN'

    @property
    def is_professor(self):
        return self.tipo_usuario == 'PROFESSOR'

    @property
    def is_admin_or_master(self):
        return self.tipo_usuario in [
            'MASTER',
            'ADMIN'
        ]

    def __str__(self):
        return self.username