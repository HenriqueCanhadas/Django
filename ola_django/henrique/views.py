from django.shortcuts import render

def henrique_view(request):
    return render(request, 'pasta_henrique/henrique.html')

def vitor_view(request):
    return render(request, 'pasta_henrique/vitor.html')