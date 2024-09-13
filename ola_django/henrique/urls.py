from django.urls import path

from . import views

app_name = 'Henrique'

urlpatterns = [
    path('', views.henrique_view, name='url_do_henrique'),
    path('vitor/', views.vitor_view, name='url_do_vitor')
]
