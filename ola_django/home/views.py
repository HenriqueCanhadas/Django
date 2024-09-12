from django.shortcuts import render

def home_view(request):
    return render(request, 'pasta_home/home.html')

def teste_view(request):
    return render(request, 'pasta_home/teste.html')