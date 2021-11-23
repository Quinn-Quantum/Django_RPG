from django.shortcuts import *
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.urls.base import *
from .models import *
from .forms import *
from django.contrib.auth.models import *

def index(request):
    user = get_object_or_404(User, username=request.user.username)
    return render(request, 'game/base.html', {'user':user})

def char_view(request):
    user = get_object_or_404(User, username=request.user.username)
    chars = CharMod.objects.filter(user = user)
    return render(request, 'game/charcter.html', {'chars': chars, 'user':user})

def kampf_view(request):
    return render(request, 'game/kampf.html')

def charChreate_view(request):
    charMaker_form = charMaker()
    if request.method == 'POST':
        charMaker_form = charMaker(request.POST)
        if login_form.is_valid():
            charName = charMaker_form.cleaned_data['charName']
            charClasse =charMaker_form.cleaned_data['charClasse']
            Char.objects.create(charName=charName,charClasse=charClasse )
    return render(request, 'game/charChreate.html', {'charMaker_form':charMaker_form})

