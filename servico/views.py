from django.shortcuts import render
from .forms import ServicoForm, ServicoFeitoForm
from .models import Servico, ServicoFeito

# Create your views here.

def test(request):
    if request.method == 'GET':

        form2 = ServicoFeitoForm()
        context = {
            
            'form2': form2
        }
        return render(request, 'test.html', context)
    
    if request.method == 'POST':
        form2 = ServicoFeitoForm(request.POST)
        if form2.is_valid():
            form2.save()
            return render(request, 'test.html', {'form2': form2})
        else:
            return render(request, 'test.html', {'form2': form2})
