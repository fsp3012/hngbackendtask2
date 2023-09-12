from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.CreateUser),
    path('user/', views.getUser),
]