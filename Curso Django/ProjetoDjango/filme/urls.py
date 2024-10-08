from django.urls import path, include
from .views import HomePage, Homefilmes, Detalhesfilme, Pesquisafilme

app_name = 'filme'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(),name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme'),
    path('login/', criar, name='login'),
    
]