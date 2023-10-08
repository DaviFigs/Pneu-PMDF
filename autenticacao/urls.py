from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),

    path('valida_login/', views.valida_login, name="valida_login"),
    path('valida_cadastro/', views.valida_cadastro, name="valida_cadastro"),

    path('trocar_senha/', views.trocar_senha, name='trocar_senha'),
    path('valida_trocar_senha/', views.valida_trocar_senha, name='valida_troca'),

]
