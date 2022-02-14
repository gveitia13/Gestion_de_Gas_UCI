from django import forms
from django.forms import ModelForm

from apps.balita.models import *


class ContratoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contrato
        fields = '__all__'
        exclude = ['date_creation', 'user', ]


class InformeIncidenciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = InformeIncidencia
        fields = '__all__'
        exclude = ['date_creation', 'user', 'balita']
        widgets = {
            'motive': forms.Textarea(
                attrs={
                    'placeholder': 'Escribe una descripción del problema',
                    'rows': 5,
                    'cols': 3,
                    'class': 'circular'
                }
            )
        }
