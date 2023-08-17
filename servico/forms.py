from django import forms
from django.forms import ModelForm
from .models import Servico, ServicoFeito

class DateInput(forms.DateInput):
    def __init__(self, attrs=None):
        attrs = attrs or {}
        attrs['type'] = 'date'
        super().__init__(attrs)
    input_type = 'date'


class ServicoForm(ModelForm):

    class Meta:
        model = Servico
        fields = ['nome','preco']

        Widget ={
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            # e numero decimal
            'preco': forms.NumberInput(attrs={'class':'form-control'}),
        
        
        
        }

class ServicoFeitoForm(ModelForm):
    class Meta:
        model = ServicoFeito
        fields = ['cliente','servico','data','valor_total', 'pago']
        execute = ['valor_total']
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'servico': forms.CheckboxSelectMultiple(),
            'data': forms.DateInput(attrs={'class':'form-control' , 'type':'date'}), 
            'valor_total': forms.NumberInput(attrs={'class':'form-control'}),
            'pago': forms.CheckboxInput(),
        }
    #soma dos servicos e limpar os campos
    def clean(self):
        cleaned_data = super().clean()
        servicos = cleaned_data.get('servico')
        valor_total = 0
        for servico in servicos: # type: ignore
            valor_total += servico.preco
        cleaned_data['valor_total'] = valor_total
        return cleaned_data
    

    
   