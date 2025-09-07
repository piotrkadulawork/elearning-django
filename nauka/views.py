from django.shortcuts import render, redirect, get_object_or_404
from .models import Lista, Slowko
from .forms import ListaForm, SlowkoForm
from django.http import HttpResponseForbidden

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

def usun_slowko(request, slowko_id):
    slowko = get_object_or_404(Slowko, id=slowko_id)
    if request.method == 'POST':
        lista_id = slowko.lista.id  # zapamiętujemy listę, żeby wrócić po usunięciu
        slowko.delete()
        return redirect('lista_slowek', lista_id=lista_id)
    # jeżeli ktoś wejdzie GET-em, to nie usuwamy — tylko blokujemy
    return HttpResponseForbidden("Nie można usuwać słówek metodą GET")

def edytuj_slowko(request, slowko_id):
    slowko = get_object_or_404(Slowko, id=slowko_id)
    if request.method == 'POST':
        form = SlowkoForm(request.POST, instance=slowko)
        if form.is_valid():
            form.save()
            return redirect('lista_slowek', lista_id=slowko.lista.id)
    else:
        form = SlowkoForm(instance=slowko)
    return render(request, 'nauka/edytuj_slowko.html', {'form': form, 'slowko': slowko})

def usun_liste(request, lista_id):
    lista = get_object_or_404(Lista, id=lista_id)
    if request.method == 'POST':
        lista.delete()  # dzięki on_delete=models.CASCADE usunie też wszystkie słówka
        return redirect('home')
    return HttpResponseForbidden("Nie można usuwać list metodą GET")

def edytuj_liste(request, lista_id):
    lista = get_object_or_404(Lista, id=lista_id)
    if request.method == 'POST':
        form = ListaForm(request.POST, instance=lista)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListaForm(instance=lista)
    return render(request, 'nauka/edytuj_liste.html', {'form': form, 'lista': lista})