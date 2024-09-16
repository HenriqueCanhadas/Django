from django.urls import path
from . import views

app_name = 'Curriculo'

urlpatterns = [
    path('', views.curriculo_henrique_view, name='url_curriculo'),
]