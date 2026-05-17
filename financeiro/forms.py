from django import forms

from .models import Mensalidade


class MensalidadeForm(forms.ModelForm):

    class Meta:

        model = Mensalidade

        fields = [

            'aluno',
            'referencia',
            'valor',
            'vencimento',
            'status',
            'data_pagamento',
            'observacoes',

        ]

        widgets = {

            'aluno': forms.Select(attrs={
                'class': 'form-select'
            }),

            'referencia': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'valor': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'vencimento': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control datepicker',
                    'placeholder': 'dd/mm/aaaa'
                }
            ),

            'status': forms.Select(attrs={
                'class': 'form-select'
            }),

            'data_pagamento': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control datepicker',
                    'placeholder': 'dd/mm/aaaa'
                }
            ),

            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

        }
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['vencimento'].input_formats = [
            '%d/%m/%Y'
        ]

        self.fields['data_pagamento'].input_formats = [
            '%d/%m/%Y'
        ]