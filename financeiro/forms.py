from django import forms

from .models import Mensalidade


class MensalidadeForm(forms.ModelForm):

    class Meta:
        model = Mensalidade

        fields = [
            'aluno',
            'referencia',
            'valor',
            'desconto',
            'valor_pago',
            'data_vencimento',
            'data_pagamento',
            'status',
            'observacoes',
        ]

        widgets = {

            'aluno': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'referencia': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'valor': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'desconto': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'valor_pago': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'data_vencimento': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'data_pagamento': forms.DateInput(
                attrs={
                    'type': 'date',
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