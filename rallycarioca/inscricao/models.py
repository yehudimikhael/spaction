from django.db import models

# Create your models here.

class Categoria(models.Model):
    tipo = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo

class Veiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    def __str__(self):
        return self.modelo

class Tp_Sangue(models.Model):
    tipo = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    cnh = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    emerg = models.CharField(max_length=100)
    pl_saude = models.CharField(max_length=100)
    al_db = models.CharField(max_length=200) ###Variável para o usuário escrever se tem alergia ou Diabetes 
    tipo_sang = models.ForeignKey(Tp_Sangue, models.PROTECT, default='tipo_sang')
    #tipo_pessoa = models.ForeignKey(Tipo_Pessoa)
    def __str__(self):
        return self.nome

class Time(models.Model):
    name = models.CharField(max_length=100)
    piloto = models.ForeignKey(Pessoa, related_name='piloto', on_delete=models.CASCADE)
    navegador = models.ForeignKey(Pessoa, related_name='navegador', on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 

class Pista(models.Model):
    nome = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Etapa(models.Model):
    pista = models.ForeignKey(Pista, on_delete=False)
    date_corrida = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.pista.nome 
        
class Evento(models.Model):
    nome = models.CharField(max_length=200)
    dateInicioInscricao  = models.DateField(auto_now=False, auto_now_add=False)
    dateFimInscricao = models.DateField(auto_now=False, auto_now_add=False)
    etapa = models.ManyToManyField(Etapa)
    def __str__(self):
        return self.nome
class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, models.PROTECT) 
    time = models.ForeignKey(Time, models.PROTECT)
    colocao = models.IntegerField()
    def __str__(self):
        return self.evento.nome   

