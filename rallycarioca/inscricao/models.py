from django.db import models

# Create your models here.

class Categoria(models.Model):
    tipo = models.CharField(max_length=100)

# class Tipo_Pessoa(models.Model):
#     tipo = models.CharField(max_length=100)

class Veiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()

class Pessoa(models.Model):
    nome_piloto = models.CharField(max_length=200)
    nome_nagevador = models.CharField(max_length=200)
    cnh = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    #tipo_san = models
    phone_piloto = models.CharField(max_length=100)
    phone_navegador = models.CharField(max_length=100)
    emerg_piloto = models.CharField(max_length=100)
    emerg_navegador = models.CharField(max_length=100)
    pl_saude = models.CharField(max_length=100)
    pl_saude = models.CharField(max_length=100)
    al_db_piloto = models.CharField(max_length=200)
    al_db_navegador = models.CharField(max_length=200) ###Variável para o usuário escrever se tem alergia ou Diabetes 
    #tipo_pessoa = models.ForeignKey(Tipo_Pessoa)