from django.shortcuts import render, redirect
from .models import ViaturasCarros, ViaturasMotos
from.models import PedidosCarros, PedidosMotos
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.contrib.messages import constants

@permission_required('admin.can_add_mod', login_url='/base/main/')
def registro_motos(request):
    if request.user.is_authenticated:
        lista_motos = ViaturasMotos.objects.all()
        context = {
            'lista_motos':lista_motos}
        return render(request, 'registro_motos.html', context)
    else:
        messages.add_message(request,constants.ERROR,'Faça login!')
        return redirect('/autenticacao/login/')
        
@permission_required('admin.can_add_mod', login_url='/base/main/')
def registro_carros(request):
    if request.user.is_authenticated:
        lista_carros = ViaturasCarros.objects.all()
        context = {
            'lista_carros':lista_carros}
        return render(request, 'registro_carros.html', context)
    else:
        messages.add_message(request,constants.ERROR,'Faça login!')
        return redirect('/autenticacao/login/')
    
def valida_registro_carros(request):
    if(request.method == 'POST'):
        id_viatura = request.POST.get('viatura') 
        pim = request.POST.get('pim') 
        quantidade = request.POST.get('quantidade')

        if len(pim.strip()) == 0 or len(pim) < 5:
            messages.add_message(request,constants.WARNING,'Preencha o PIM corretamente')
            return redirect('/registro/registro_carros/')
        elif len(quantidade.strip()) == 0:
            messages.add_message(request,constants.WARNING,'Preencha a quantidade corretamente')
            return redirect('/registro/registro_carros/')
        
        pedido = PedidosCarros.objects.filter(pim = pim)
        if len(pedido) > 0:
            messages.add_message(request,constants.WARNING,'Este pim já existe')
            return redirect('/registro/registro_carros/')
        elif len(pedido) == 0:
            pedido = PedidosCarros(
                                    pim = pim,
                                    quantidade = quantidade,
                                    viatura_id = id_viatura)
            pedido.save()
            messages.add_message(request,constants.SUCCESS,'Registro feito com sucesso')
            return redirect('/visualizacao/visualizar_carros/')
    else:
        messages.add_message(request,constants.ERROR,'Você não possui acesso a essa URL')
        return redirect('/base/main/')
    
def valida_registro_motos(request):
    if(request.method == 'POST'):
        id_viatura = request.POST.get('viatura') 
        pim = request.POST.get('pim') 
        quantidade = request.POST.get('quantidade')

        if len(pim.strip()) == 0 or len(pim.strip()) < 5:
            messages.add_message(request,constants.WARNING,'Preencha o PIM corretamente')
            return redirect('/registro/registro_motos/')
        elif len(quantidade.strip()) == 0:
            messages.add_message(request,constants.WARNING,'Preencha a QUANTIDADE corretamente!')
            return redirect('/registro/registro_motos/')
        
        pedido = PedidosCarros.objects.filter(pim = pim)
        if len(pedido) > 0:
            messages.add_message(request,constants.WARNING,'Este pim já existe!')
            return redirect('/registro/registro_motos/')
        elif len(pedido) == 0:
            pedido = PedidosMotos(
                                    pim = pim,
                                    quantidade = quantidade,
                                    viatura_id = id_viatura)
            pedido.save()
            messages.add_message(request,constants.SUCCESS,'Registro feito com sucesso')
            return redirect('/visualizacao/visualizar_motos')
    else:
        messages.add_message(request,constants.ERROR,'Você não possui acesso a essa URL')
        return redirect('/base/main/')