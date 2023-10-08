from django.shortcuts import render
from registro.models import *
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required

@login_required(login_url="/autenticacao/login/")
def visualizar_motos(request):
    lista_pedidos_motos = PedidosMotos.objects.all()
    context = {
            'lista_pedidos_motos':lista_pedidos_motos}
    return render(request, 'visualizacao_motos.html', context)

@login_required(login_url="/autenticacao/login/")
def visualizar_carros(request):
    lista_pedidos_carros = PedidosCarros.objects.all()
    context = {
        'lista_pedidos_carros':lista_pedidos_carros}
    return render(request, 'visualizacao_carros.html', context)