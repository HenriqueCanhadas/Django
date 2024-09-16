from django.urls import path
from . import views

app_name = 'Projeto'

urlpatterns = [
    path('', views.projeto_canhadas_view, name='url_projeto'),
]