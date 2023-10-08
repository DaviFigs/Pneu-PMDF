from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as logon, logout as logouts
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib import messages
from django.contrib.messages import constants

#funções de call para os templates

@permission_required('add_logentry', login_url='/base/main/')
def cadastro(request):
    if request.user.is_authenticated:
        return render(request,'cadastro.html')
    else:
        messages.add_message(request,constants.WARNING,'Faça login!')
        return redirect('/autenticacao/login/')

def login(request):
    if request.user.is_authenticated:
        messages.add_message(request,constants.WARNING,'Você já está logado')
        return redirect('/base/main/')
    return render(request,'login.html')

@login_required(login_url="/autenticacao/login/")
def trocar_senha(request):
    return render(request, 'trocar_senha.html')
    
#funções de validação

def valida_cadastro(request):
    if(request.method != 'POST'):
        messages.add_message(request,constants.ERROR,'Você não possui acesso a essa URL')
        return redirect('/autenticacao/login/')
    else:
        try:
            usuario = request.POST.get('usuario')
            senha = request.POST.get('senha')
            conf_senha = request.POST.get('conf_senha')
            permissao = request.POST.get('permissao')
            if(senha != conf_senha):
                messages.add_message(request,constants.WARNING,'As senhas não coincidem!')
                return redirect('/autenticacao/cadastro/')
            elif len(usuario.strip()) == 0:
                messages.add_message(request,constants.WARNING,'Preencha os campos corretamente!')
                return redirect('/autenticacao/cadastro/')
            elif len(senha) <8:
                messages.add_message(request,constants.WARNING,'A senha deve conter ao menos 8 caracteres!')
                return redirect('/autenticacao/cadastro/')
            
            user = User.objects.filter(username = usuario)
            if(len(user) > 0):
                messages.add_message(request,constants.ERROR,'Já existe um usuário com este nome!')
                return redirect('/autenticacao/cadastro/')
            
            elif(len(user)) == 0:
                user = User.objects.create_user(username = usuario, password=senha)
                if(permissao == '1'):
                    user.user_permissions.add(74)
                user.save()
                messages.add_message(request,constants.SUCCESS,'Usuário cadastrado com sucesso')
                return redirect('/base/main/')   
        except:
            messages.add_message(request,constants.ERROR,'Erro do sistema!')
            return redirect('/autenticacao/cadastro/')

def valida_login(request):
    if(request.method != 'POST'):
            messages.add_message(request,constants.ERROR,'Você não possui acesso a essa URL')
            return redirect('/base/main/')
    else:
        try:
            usuario = request.POST.get('usuario')
            senha = request.POST.get('senha')     
            user = authenticate(username = usuario, password = senha)
            if user == None:
                messages.add_message(request,constants.WARNING,'Usuário ou senha incorretos!')
                return redirect('/autenticacao/login/')        
            elif user is not None:
                logon(request, user)
                return redirect('/base/main/')
        except:
            messages.add_message(request,constants.ERROR,'Erro do sistema!')
            return redirect('/autenticacao/login/')
        
def logout(request):
    if request.user.is_authenticated:
        logouts(request)
        return redirect('/autenticacao/login/')
    else:
        messages.add_message(request,constants.ERROR,'Usuário já fora de sessão!')
        return redirect('/autenticacao/login/')

def valida_trocar_senha(request):
    if(request.method != 'POST'):
            messages.add_message(request,constants.ERROR,'Você não possui acesso a essa URL')
            return redirect('/base/main/')
    else:
        try:   
            nova_senha = request.POST.get('nova_senha')
            if(len(nova_senha) < 8 ):
                messages.add_message(request,constants.WARNING,'A sua nova senha deve conter ao menos 8 carcteres!')
                return redirect('/autenticacao/trocar_senha/')
            else:
                senha_atual = request.POST.get('senha_atual')
                usuario = request.POST.get('user')
                conf_user = authenticate(username = usuario, password = senha_atual)
                if conf_user == None:
                    messages.add_message(request,constants.ERROR,'Seu usuário ou senha estão incorretos!')
                    return redirect('/autenticacao/trocar_senha/')

                user = User.objects.get(username = request.user.username)
                nova_senha = request.POST.get('nova_senha')
                user.set_password(nova_senha)
                user.save()
                logouts(request)
                messages.add_message(request,constants.SUCCESS,'Sua senha foi trocada, faça login novamente!')
                return redirect('/autenticacao/login/')
        except:
            messages.add_message(request,constants.ERROR,'Erro do sistema!')
            return redirect('/autenticacao/cadastro/') 