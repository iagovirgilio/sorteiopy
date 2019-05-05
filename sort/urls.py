from django.urls import path
from . import views


urlpatterns = [
    path('', views.sorteador, name='sorteador'),
    path('sorteio', views.sorteio, name='sorteio'),
]
