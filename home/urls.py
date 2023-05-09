from django.urls import path
from . import views

urlspattern = [
    path('view/', views.home, name="home")
    
]