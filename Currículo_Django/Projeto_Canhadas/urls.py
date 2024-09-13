from django.urls import path
from . import views

urlpatterns = [
    path('', views.projeto_canhadas_view),
]