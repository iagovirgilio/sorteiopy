from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.sorteador, name='sorteador'),
    path('sorteio', views.sorteio, name='sorteio'),
    path('sobre', views.sobre, name='sobre'),
]
