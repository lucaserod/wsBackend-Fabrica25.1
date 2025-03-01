from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from .models import Usuario
from .forms import UsuarioForm

def register_view(request):
    if request.method == 'GET':
        form = UsuarioForm()
        return render(request, 'register.html', {'form': form})
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            request.status_code = 201
            return redirect('listar')


def list_view(request):
    usuarios = Usuario.objects.all()
    if usuarios:
        return render(request, 'list.html', {'usuarios': usuarios})
    return render(request, 'list.html')


def detail_view(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if usuario:
        return render(request, 'detail.html', {'usuario': usuario})


# Essas duas views functions nos veremos amanhã no inicio da aula
def delete_view(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if usuario:
        usuario.delete()
        #  204 No Content Explicação: O servidor processou o pedido com sucesso, mas não devolveu nenhum conteúdo.
        request.status_code = 204
        return redirect('listar')


def update_view(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuario)
        return render(request, 'update.html', {'usuario': usuario, 'form': form})
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar')



def home_view(request):
    return render(request, 'home.html')