from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ["nombre", "email", "website", "comentarios"]
        #fields = '__all__'

#creación de formularios.
class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class loginForm(AuthenticationForm):
    class Meta:
        model = User 
        fields = ['username','password','remember_me']
        username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'newsletter-form col-md-12 col-lg-6'}))
        password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'newsletter-form col-md-12 col-lg-3', 'data-toggle': 'password', 'id': 'password', 'name': 'password',}))
        remember_me = forms.BooleanField(required=False)
    
#    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'container'}))
#    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'contact-form'}))
#    comentarios = forms.CharField(widget=forms.TextInput(attrs={'class': 'row'}))

#pip -m install django_crispy_forms

#Archivo settings.py del proyecto, agregamos la app y las variables