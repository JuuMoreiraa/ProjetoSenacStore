from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    meu_nome = 'Ju Moreira'
    sexo = 'F'
    context = {
        'nome': meu_nome, 
        'artigo': 'o' if sexo == 'M' else 'a'
        }
    return render(request,'index.html', context)

def teste(request):
    depto = ['Armazenamento', 'Mise en place', 'Cozinha', 'Finalização', 'Higiene e limpeza']
    context = {'departamentos': depto}
    return render(request,'teste.html', context)