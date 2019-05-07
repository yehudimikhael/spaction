from django.contrib import admin

from .models import Inscricao, Time, Categoria, Etapa, Evento, Pessoa, Pista, Tp_Sangue, Veiculo

# Register your models here.

admin.site.register(Inscricao)
admin.site.register(Time)
admin.site.register(Categoria)
admin.site.register(Etapa)
admin.site.register(Evento)
admin.site.register(Pessoa)
admin.site.register(Pista)
admin.site.register(Tp_Sangue)
admin.site.register(Veiculo)