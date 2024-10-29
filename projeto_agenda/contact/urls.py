from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('contact/create', views.create, name='create'),
    path('contact/<int:contact_id>/read', views.contact, name='contact'),
    path('contact/<int:contact_id>/update', views.contact, name='contact'),
    path('contact/<int:contact_id>/delete', views.contact, name='contact'),

    # path('<int:contact_id>/', views.contact, name='contact'),

    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
