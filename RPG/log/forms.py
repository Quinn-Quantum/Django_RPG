from django import forms
from django.contrib.auth.models import *
#Forms die sich auf models bezihen werden mit forms.Modelform deklariert
#normale Forms einfach forms.Forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50, label = 'Username eintragen' ,required = True)
    password = forms.CharField(min_length=5, max_length = 16, label='Passwort eintragen', widget=forms.PasswordInput, required = True)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists(): #Usernamen aus der DB auslesen und vergleichen, bechaten Groß und Kleinschreibung nicht
            raise froms.ValidationError('Username existiert schon')
        return username

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username eintragen', required = True)
    password = forms.CharField(min_length=5, max_length=16, label='Passwort eintragen', widget=forms.PasswordInput, required = True)