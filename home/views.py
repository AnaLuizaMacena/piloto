from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import ContatoForm
from .forms import ProdutoForm

def index (request):
    return render (request, 'index.html')

def sobre (request):
    return render (request, 'sobre.html')

def contato (request):
    form = ContatoForm()
    contexto = {
        'form': form,
    }
    return render (request, 'contato.html', contexto)

def exibir_item(request,id):
    return render(request,"exibir_item.html",{'id':id})

def perfil(request,usuario):
    return render(request,"perfil.html",{'usuario':usuario})

def diadasemana(request,id):
    dias= {
            1: 'Domingo',
            2: 'Segunda-feira',
            3: 'Terça-feira',
            4: 'Quarta-feira',
            5: 'Quinta-feira',
            6: 'Sexta-feira',
            7: 'Sabado'
        }
    dia= dias.get (id,None)

    if dia:
        return render (request, "diadasemana.html",{'dia': dia})
    else:
        return render (request, "diadasemana.html",{"dia": "dia invalido"})
    
def form_produto(request):
    form = ProdutoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'produto/formulario.html', contexto)

def produtos(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'quantidade': 10, 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'quantidade': 10, 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'quantidade': 10, 'preco': '80,00'},
            {'id': 4, 'nome': 'Mouse', 'quantidade': 10, 'preco': '40,00'},
            {'id': 5, 'nome': 'Impressora', 'quantidade': 10, 'preco': '600,00'},
            {'id': 6, 'nome': 'Scanner', 'quantidade': 10, 'preco': '700,00'},
            {'id': 7, 'nome': 'Câmera Web', 'quantidade': 10, 'preco': '150,00'},
            {'id': 8, 'nome': 'Headset', 'quantidade': 10, 'preco': '120,00'},
            {'id': 9, 'nome': 'Pendrive 32GB', 'quantidade': 10, 'preco': '30,00'},
            {'id': 10, 'nome': 'HD Externo 1TB', 'quantidade': 10, 'preco': '350,00'},
            {'id': 11, 'nome': 'Estabilizador', 'quantidade': 10, 'preco': '200,00'},
            {'id': 12, 'nome': 'Switch 8 portas', 'quantidade': 10, 'preco': '180,00'},
            {'id': 13, 'nome': 'Roteador Wi-Fi', 'quantidade': 10, 'preco': '220,00'},
        ],
    }
    return render(request, 'produto/lista.html', contexto)

def detalhes_produto(request,id):
    return render(request,"produto/detalhes.html",{'id':id})

def editar_produto(request, id):
    form = ProdutoForm()
    contexto = {
        'form': form,
            }
    return render(request,"produto/formulario.html", contexto)

def excluir_produto(request,id):
    return render(request,"produto/excluir.html",{'id':id})

