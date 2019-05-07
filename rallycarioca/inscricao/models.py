from django.db import models

# Create your models here.

class Categoria(models.Model):
    tipo = models.CharField(max_length=100)

class Veiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
class Tp_Sangue(models.Model):
    tipo = models.CharField(max_length=100)

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    cnh = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    emerg = models.CharField(max_length=100)
    pl_saude = models.CharField(max_length=100)
    al_db = models.CharField(max_length=200) ###Variável para o usuário escrever se tem alergia ou Diabetes 
    tipo_sang = models.ForeignKey(Tp_Sangue, models.PROTECT, default='tipo_sang')
    #tipo_pessoa = models.ForeignKey(Tipo_Pessoa)

class Time(models.Model):
    piloto = models.ForeignKey(Pessoa, related_name='piloto', on_delete=models.CASCADE)
    navegador = models.ForeignKey(Pessoa, related_name='navegador', on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

class Pista(models.Model):
    nome = models.CharField(max_length=200)
    local = models.CharField(max_length=200)

class Etapa(models.Model):
    pista = models.ForeignKey(Pista, on_delete=False)
    date_corrida = models.DateField(auto_now=False, auto_now_add=False)

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    dateInicioInscricao  = models.DateField(auto_now=False, auto_now_add=False)
    dateFimInscricao = models.DateField(auto_now=False, auto_now_add=False)
    etapa = models.ManyToManyField(Etapa)
class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, models.PROTECT) 
    time = models.ForeignKey(Time, models.PROTECT)
    colocao = models.IntegerField()    

