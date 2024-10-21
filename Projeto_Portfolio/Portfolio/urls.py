from django.urls import path
from . import views

app_name = 'Portfolio'

urlpatterns = [
    path('', views.portfolio_henrique_view, name='url_portfolio'),
]