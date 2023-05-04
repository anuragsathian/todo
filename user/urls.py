from django.urls import path
from .import views

urlpatterns = [

    path('create account',views.signup),
    path('index',views.index),
    path('login',views.login),
]