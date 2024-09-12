from django.urls import path

from . import views

urlpatterns = [
    path('', views.henrique_view),
    path('vitor/', views.vitor_view)
]
