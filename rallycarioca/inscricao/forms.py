from django import forms 
from .models import *

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa 
        fields = ["nome", "cnh", "phone", "emerg", "pl_saude", "al_db", "tipo_sang"]