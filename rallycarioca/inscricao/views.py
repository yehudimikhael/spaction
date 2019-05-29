from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template, Context
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def inscricao(request):
    return render(request, 'inscricao.html')