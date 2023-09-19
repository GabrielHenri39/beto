from django.shortcuts import render
from .forms import ServicoForm, ServicoFeitoForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='auth/login') # type: ignore
def test(request):
    if request.method == 'GET':
       form = ServicoForm() 
       return render(request, 'test.html', {'form': form})
    
    elif request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'test.html', {'form': form})
        else:
            return render(request, 'test.html', {'form': form})
    
@login_required(login_url='auth/login')    # type: ignore
def test2(request):
    if request.method == 'GET':
       form = ServicoFeitoForm() 
       
       return render(request, 'test2.html', {'form': form})
    
    elif request.method == 'POST':
        form = ServicoFeitoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'test2.html', {'form': form})
        else:
            return render(request, 'test2.html', {'form': form})