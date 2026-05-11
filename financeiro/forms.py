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

            'vencimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'status': forms.Select(attrs={
                'class': 'form-select'
            }),

            'data_pagamento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

        }