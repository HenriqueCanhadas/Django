from django.shortcuts import render

def henrique_view(request):

    context = {
        'text' : 'Olá Henrique',
        'title' : 'Henrique'
    }

    return render(request, 'pasta_henrique/henrique.html', context)

def vitor_view(request):
    context = {
        'text' : 'Olá Vitor',
        'title' : 'Vitor'
    }
    return render(request, 'pasta_henrique/vitor.html', context)