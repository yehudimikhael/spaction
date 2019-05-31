from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inscricao/', views.inscricao, name='inscricao'),
    path('accountss/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cadastro_pessoa/', views.cadastro_pessoa, name='cadastro_pessoa')
]