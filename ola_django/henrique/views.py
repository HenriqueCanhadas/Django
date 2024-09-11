from django.shortcuts import render
from django.http import HttpResponse

def henrique_view(request):
    return HttpResponse("Deu Certo, Funcionou!!")