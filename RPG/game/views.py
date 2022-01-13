from django.shortcuts import *
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.urls.base import *
from .models import *
from .forms import *
from django.contrib.auth.models import *
from .gegner import *
from .ankreifer import *

def index(request):
    user = get_object_or_404(User, username=request.user.username)
    return render(request, 'game/base.html', {'user':user})

def char_view(request):
    user = get_object_or_404(User, username=request.user.username)
    chars = CharMod.objects.filter(user = user)
    return render(request, 'game/charcter.html', {'chars': chars, 'user':user})

def kampf_view(request):
    if request.user.is_authenticated:
        gegner = Gegner()
    user = get_object_or_404(User, username=request.user.username)
    chars = CharMod.objects.filter(user=user)
    spieler = CharMod.objects.get(user=request.user)
    level = 1
    for i in chars:
        if i.user == request.user:
            ankreifer = Ankreifer() #damit die Werte des Chars suaber übergeben werden können
            ankreifer.atk = i.charATK
            ankreifer.leben = i.charLeben
            level = i.charLevel

    if level < 2:
        enemy = EnemyMod.objects.filter(id =1)
        for j in enemy:
            if j.id == 1:
                gegner.name = j.enemyName
                gegner.atk = j.enemyATK
                gegner.leben = j.enemyLeben
    return render(request, 'game/kampf.html', {'gegner':gegner, 'chars': chars, 'user':user, 'ankreifer':ankreifer, 'spieler':spieler })

def charChreate_view(request):
    charMaker_form = charMaker()
    maker=charMaker_form.save(commit=False)
    if request.method == 'POST':
        charMaker_form = charMaker(request.POST)
        if charMaker_form.is_valid():
            maker=charMaker_form.save(commit=False)
            maker.user=request.user
            maker.charEP=0
            maker.charLevel=1
            maker.besigtegegner =0
            maker.charLeben = 50
            if maker.charClasse == 'Krieger':
                maker.charATK = 15
                maker.charDEF = 10
                maker.charMAN = 10
            elif maker.charClasse == 'Magier':
                maker.charATK = 10
                maker.charDEF = 10
                maker.charMAN = 15
            else:
                maker.charATK = 10
                maker.charDEF = 10
                maker.charMAN = 10
            maker.save()
            if maker:
                return redirect(reverse( 'game:char'))
    return render(request, 'game/charChreate.html', {'charMaker_form':charMaker_form, 'maker': maker})

def sieg_view (request):
    user = get_object_or_404(User, username=request.user.username)
    chars = CharMod.objects.filter(user=user)
    for i in chars:
        if i.user == request.user:
            i.besigtegegner += 1
            i.charEP += 10
            if i.charEP == 100:
                i.charLevel += 1
                #Level up
                if i.charClasse == 'Magier':
                    i.charMAN += 5
                    i.charDEF += 2
                    i.charATK += 2
                    i.charLeben += 5
                    i.charEP = 0
                else:
                    i.charMAN += 2
                    i.charDEF += 2
                    i.charATK += 5
                    i.charLeben += 5
                    i.charEP = 0

            i.save()
    return redirect(reverse('game:char'), {'user':user, 'chars':chars})

def niederlage_view(request):
    return redirect(reverse('game:char'))

