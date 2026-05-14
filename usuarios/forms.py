from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class UsuarioForm(UserCreationForm):

    class Meta:

        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'telefone',
            'foto',
            'tipo_usuario',
            'password1',
            'password2',
        ]

        widgets = {

            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'foto': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'tipo_usuario': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

        }

    def __init__(self, *args, **kwargs):

        usuario_logado = kwargs.pop(
            'usuario_logado',
            None
        )

        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })

        # REGRA DE PERMISSÃO

        if usuario_logado:

            # ADMIN não pode criar MASTER

            if usuario_logado.tipo_usuario == 'ADMIN':

                self.fields['tipo_usuario'].choices = [
                    ('PROFESSOR', 'Professor')
                ]

            # MASTER pode criar ADMIN e PROFESSOR

            elif usuario_logado.tipo_usuario == 'MASTER':

                self.fields['tipo_usuario'].choices = [
                    ('ADMIN', 'Administrador'),
                    ('PROFESSOR', 'Professor')
                ]