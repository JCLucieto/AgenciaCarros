from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import auth

def cadastrar_usuario(request):
    if request.method == 'POST':
        usuarioform = UserCreationForm(request.POST)
        if usuarioform.is_valid():
            usuarioform.save()
            return redirect('login')
    else:
       usuarioform = UserCreationForm()
    return render (request, 'cadastrar_usuario.html', {'usuarioform' : usuarioform})


def login(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        senha   = request.POST['password']
        usuario_logado = authenticate(request, username=usuario, password=senha)
        if usuario_logado is not None:
            auth.login(request,usuario_logado)
            return redirect ('consultar_carros')
        else:
             loginform = AuthenticationForm()
    else:
        loginform = AuthenticationForm()
    return render (request, 'login.html', {'loginform' : loginform})


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    loginform = AuthenticationForm()
    return render (request, 'login.html', {'loginform' : loginform})