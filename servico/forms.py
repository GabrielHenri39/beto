from django.forms import ModelForm
from django import forms
from .models import Servico , ServicoFeito
from datetime import date
from .form_s import ServicoCheckbox
# Here are some code snippets from other files of the repo:

class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = ['servico','preco']
        widgets = {
            'servico': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ServicoFeitoForm(forms.ModelForm):
    class Meta:
        model = ServicoFeito
        fields = ['cliente', 'servico', 'data', 'valor_total', 'pago']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'servico': ServicoCheckbox(), # type: ignore
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': date.today}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'pago': forms.CheckboxInput(),
        }

  