from django import forms

from .models import Aula


class AulaForm(forms.ModelForm):

    class Meta:
        model = Aula

        fields = [
            'modalidade',
            'professor',
            'data',
            'horario_inicio',
            'horario_fim',
            'observacoes',
        ]

        widgets = {

            'modalidade': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'professor': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'data': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control datepicker',
                    'placeholder': 'dd/mm/aaaa'
                }
            ),


            'horario_inicio': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),

            'horario_fim': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),

            'observacoes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),

        }
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['data'].input_formats = [
            '%d/%m/%Y'
        ]