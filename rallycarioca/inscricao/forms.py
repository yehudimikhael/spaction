from django import forms 
from .models import *

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa 
        fields = ["nome", "cnh", "phone", "emerg", "pl_saude", "al_db", "tipo_sang"]
        labels = {
            "nome": "Nome", 
            "cnh": "CNH",
            "phone": "Telefone", 
            "emerg": "Numero de Telefone para Emergencia", 
            "pl_saude": "Plano de Saude", 
            "al_db": "Alergia ou Diabetes(Caso positivo citar)", 
            "tipo_sang": "Tipo sanguineo"
        }
class PessoaNavegador(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ["nome", "cnh", "phone", "emerg", "pl_saude", "al_db", "tipo_sang"]
        labels = {
            "nome": "Nome", 
            "cnh": "Numero Identidade",
            "phone": "Telefone", 
            "emerg": "Numero de Telefone para Emergencia", 
            "pl_saude": "Plano de Saude", 
            "al_db": "Alergia ou Diabetes(Caso positivo citar)", 
            "tipo_sang": "Tipo sanguineo"
        }