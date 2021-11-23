from django import forms
from django.contrib.auth.models import *
from .models import *
from django.forms.models import *




class charMaker(forms.Form):
        chrNameT= forms.CharField(min_length=5, max_length = 50, label='Name', required = True)
        CHOICES = (('Klasse wählen','Klasse wählen'),('Magier','Magier'),('Krieger','Krieger'))
        field = forms.ChoiceField(choices=CHOICES)







