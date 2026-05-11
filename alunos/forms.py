from django import forms

from .models import Aluno


class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno

        fields = [
            'graduacao',
            'nome',
            'foto',
            'data_nascimento',
            'telefone',
            'email',
            'peso',
            'altura',
            'tempo_graduacao',
            'status',
            'observacoes',
        ]

        widgets = {

            'data_nascimento': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'graduacao': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'foto': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'peso': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'altura': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'tempo_graduacao': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),


            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'observacoes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),

        }