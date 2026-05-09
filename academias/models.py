from django.db import models


class Academia(models.Model):
    nome = models.CharField(max_length=150)
    logo = models.ImageField(
        upload_to='logos/',
        blank=True,
        null=True
    )

    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    endereco = models.CharField(max_length=255)

    ativa = models.BooleanField(default=True)

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome