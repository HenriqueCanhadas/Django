"""
URL configuration for Currículo_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

def view(request):
    context = {
    'title' : 'Página inicial',
    }
    return render(request, 'global/index.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view, name='url_inicial'),
    path('Curriculo/', include('Currículo_Henrique.urls')),
    path('Projeto/', include('Projeto_Canhadas.urls')),
]
