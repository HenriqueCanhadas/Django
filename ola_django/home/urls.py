from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view),
    path('teste/', views.teste_view)
]