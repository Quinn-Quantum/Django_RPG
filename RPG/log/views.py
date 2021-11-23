from django.shortcuts import *
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.urls.base import *
from .forms import *
from django.contrib.auth.models import *


def index(request):
    return render(request, 'log/index.html')

def register_view(request):
    register_form = RegisterForm()
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username'] #per KeyWord eintrag in eine Variable speichern
            password = register_form.cleaned_data['password']  #es gibt beim regrister zwei passwörter in der Form von django also Password1 oder 2 verwänden
            User.objects.create_user(username=username, password=password)
            user = authenticate(request, username=username, password=password) #beim audentifiezieren die Variablen mit den einträgen in der DB abgleichen
            if user:
                login(request, user) #Existiert der User wird er eingelogt
                return redirect(reverse('game:index'))
    return render(request, 'log/register.html', {'register_form':register_form})

def login_view(request):
    login_form =LoginForm()
    if request.method == "POST":   #Daten beim einlogken zu DB senden um sie zu vergleichen
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('game:index'))
    return render(request, 'log/login.html',{'login_form':login_form})

def logout_view(request):
    logout(request)
    return redirect(reverse('log:index'))