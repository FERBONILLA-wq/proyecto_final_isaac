# en el archivo bebidas/forms.py

from django import forms
from .models import Bebida

class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ['nombre', 'descripcion', 'imagen', 'precio']
