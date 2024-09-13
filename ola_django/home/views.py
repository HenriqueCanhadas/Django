from django.shortcuts import render
from home.data import posts



def home_view(request):

    context = {
        'text' : 'Olá Home',
        'title' : 'HOME'
    }

    return render(request, 'pasta_home/home.html', context)

def teste_view(request):

    context = {
        'text' : 'Olá Teste',
        'title' : 'TESTE',
        'posts' : posts
    }

    return render(request, 'pasta_home/teste.html',context)