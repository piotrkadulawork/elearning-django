from django.shortcuts import render, redirect, get_object_or_404
from .models import Lista, Slowko
from .forms import ListaForm, SlowkoForm

def home(request):
    listy = Lista.objects.all()
    return render(request, 'nauka/home.html', {'listy': listy})

def nowa_lista(request):
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListaForm()
    return render(request, 'nauka/nowa_lista.html', {'form': form})

def lista_slowek(request, lista_id):
    lista = get_object_or_404(Lista, id=lista_id)
    slowka = lista.slowka.all()
    if request.method == 'POST':
        form = SlowkoForm(request.POST)
        if form.is_valid():
            slowko = form.save(commit=False)
            slowko.lista = lista
            slowko.save()
            return redirect('lista_slowek', lista_id=lista.id)
    else:
        form = SlowkoForm()
    return render(request, 'nauka/lista_slowek.html', {
        'lista': lista,
        'slowka': slowka,
        'form': form
    })