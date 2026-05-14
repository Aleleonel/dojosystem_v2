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
                attrs={'class': 'form-control'}
            ),

            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'username': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),

            'telefone': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'foto': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),

            'tipo_usuario': forms.Select(
                attrs={'class': 'form-select'}
            ),

        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )


class UsuarioUpdateForm(forms.ModelForm):

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
        ]

        widgets = {

            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'username': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),

            'telefone': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'foto': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),

            'tipo_usuario': forms.Select(
                attrs={'class': 'form-select'}
            ),

        }