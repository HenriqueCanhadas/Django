from django.shortcuts import render
from django.http import HttpResponse

def home_views(request):
    return HttpResponse("Esta e minha pagina home")