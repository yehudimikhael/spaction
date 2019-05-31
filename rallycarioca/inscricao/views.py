from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Template, Context
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import * 
# Create your views here.

def index(request):
    count = User.objects.count()
    # return render(request, 'index.html', {'count': count})
    return render(request, 'home/index.html')

def inscricao(request):
    form = PessoaForm()
    return render(request, 'inscricao/cadastro_pessoa.html', { 'form': form })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscricao')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
def cadastro_pessoa(request):
    form = PessoaForm()
    return render(request, 'inscricao/cadastro_pessoa.html', { 'form': form })