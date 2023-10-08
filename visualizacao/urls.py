from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('visualizar_motos/', views.visualizar_motos, name='visualizar_motos'),
    path('visualizar_carros/', views.visualizar_carros, name='visualizar_carros'),
]