from django.db import models
from django.contrib.auth.models import User
from django.urls.base import *
from django.conf import settings
# Create your models here.
class CharMod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    charName = models.CharField(max_length=50)
    charClasse = models.CharField(max_length=50)
    charATK = models.IntegerField(null=True)
    charDEF = models.IntegerField(null=True)
    charMAN = models.IntegerField(null=True)
    charEP = models.IntegerField(null=True)
    charLevel= models.IntegerField(null=True)
    besigtegegner= models.IntegerField(null=True)
    charLeben = models.IntegerField(null=True)
