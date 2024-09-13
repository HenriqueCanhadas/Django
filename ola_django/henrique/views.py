from django.shortcuts import render

def henrique_view(request):

    context = {
        'text' : 'Olá henrique',
        'title' : 'Henrique'
    }

    return render(request, 'pasta_henrique/henrique.html', context)

def vitor_view(request):
    context = {
        'text' : 'Olá vitor',
        'title' : 'Vitor'
    }
    return render(request, 'pasta_henrique/vitor.html', context)