from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ["nombre", "email", "comentarios"]
        #fields = '__all__'

#    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'container'}))
#    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'contact-form'}))
#    comentarios = forms.CharField(widget=forms.TextInput(attrs={'class': 'row'}))

#pip -m install django_crispy_forms

#Archivo settings.py del proyecto, agregamos la app y las variables