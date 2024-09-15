from django.urls import path

from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.home_view, name='url_da_home'),
    path('<int:post_id>/', views.post_view, name='post'),
    path('teste/', views.teste_view, name='url_de_teste')
]