from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('registro_motos/', views.registro_motos, name='registro_motos'),
    path('registro_carros/', views.registro_carros, name='registro_carros'),

    path('valida_registro_carros/', views.valida_registro_carros, name="valida_carros"),
    path('valida_registro_motos/', views.valida_registro_motos, name="valida_motos"),
]