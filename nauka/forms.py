from django import forms
from .models import Lista, Slowko

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['nazwa']

class SlowkoForm(forms.ModelForm):
    class Meta:
        model = Slowko
        fields = ['angielski', 'polski']