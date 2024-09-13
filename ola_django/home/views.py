from django.shortcuts import render

def home_view(request):

    context = {
        'text' : 'Olá Home',
        'title' : 'HOME'
    }

    return render(request, 'pasta_home/home.html', context)

def teste_view(request):

    context = {
        'text' : 'Olá Teste',
        'title' : 'TESTE'
    }

    return render(request, 'pasta_home/teste.html',context)