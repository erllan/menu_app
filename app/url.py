from django.urls import path
from .views import main

urlpatterns = [
    path('', main, name='main'),
    path('<str:name>', main, name='main_name'),
]