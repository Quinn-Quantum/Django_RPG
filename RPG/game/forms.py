from django import forms
from django.contrib.auth.models import *
from .models import *
from django.forms.models import *
from django.forms import *


class charMaker(ModelForm):
    CHOICES = (("Krieger", "Krieger"), ("Magier", "Magier") )
    charClasse = ChoiceField(choices=CHOICES)

    class Meta:
        model = CharMod
        fields = ('charName', 'charClasse')
        labels = {
            'charName': 'Name deines Avatas',
            'charClasse': 'Classe deines Avatas',

        }










