from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('doctors', views.doctors, name='doctors'),
    path('list_services', views.list_services, name='list_services'),
]