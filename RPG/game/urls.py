from . import views
from django.urls import path

app_name='game'
urlpatterns = [
    path('base/',views.index, name='index'),
    path('charcter/',views.char_view, name='char'),
    path('kampf/',views.kampf_view, name='kampf'),
    path('charChreate/', views.charChreate_view, name='charChreate'),
    path('sieg/', views.sieg_view, name='sieg'),
    path('niederlage/', views.niederlage_view, name='niederlage'),


]