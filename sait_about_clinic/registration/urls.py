from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('user_authentication', views.user_authentication, name='user_authentication')
]




