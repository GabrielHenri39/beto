from django.forms import ModelForm
from django import forms
from .models import Servico , ServicoFeito
from datetime import date
from .form_s import ServicoCheckbox
# Here are some code snippets from other files of the repo:

class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = ['nome','preco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ServicoFeitoForm(forms.ModelForm):
    class Meta:
        model = ServicoFeito
        fields = ['cliente', 'servico', 'data', 'valor_total', 'pago']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'servico': ServicoCheckbox(),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': date.today}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'pago': forms.CheckboxInput(),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     # Recupere as escolhas do campo 'servico' e atribua o atributo 'data-preco' com base no ID do serviço
    #     for field_name, field in self.fields.items():
    #         if field_name == 'servico':
    #             servico_ids = [str(choice[0]) for choice in field.choices]
    #             for servico_id in servico_ids:
    #                 try:
    #                     servico = Servico.objects.get(id=servico_id)
    #                     field.widget.attrs[f'data-preco-{servico_id}'] = servico.preco
    #                 except Servico.DoesNotExist:
    #                     pass




