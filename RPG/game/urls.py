from . import views
from django.urls import path

app_name='game'
urlpatterns = [
    path('base/',views.index, name='index'),
    path('charcter/',views.char_view, name='char'),
    path('kampf/',views.kampf_view, name='kampf'),
    path('charChreate/', views.charChreate_view, name='charChreate'),


]