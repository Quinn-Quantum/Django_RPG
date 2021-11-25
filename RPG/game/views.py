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
    maker=charMaker_form.save(commit=False)
    if request.method == 'POST':
        charMaker_form = charMaker(request.POST)
        if charMaker_form.is_valid():
            maker=charMaker_form.save(commit=False)
            maker.user=request.user
            if maker.charClasse == 'Kriger':
                maker.charATK = 15
                maker.charDEF =10
                maker.charMAN = 10
            elif maker.charClasse == 'Magier':
                maker.charATK = 10
                maker.charDEF =10
                maker.charMAN = 15
            else:
                maker.charATK = 10
                maker.charDEF = 10
                maker.charMAN = 10
            maker.save()
            if maker:
                return redirect(reverse( 'game:char'))
    return render(request, 'game/charChreate.html', {'charMaker_form':charMaker_form, 'maker': maker})

