from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.sorteador, name='sorteador'),
    path('sorteio', views.sorteio, name='sorteio'),
    # url(r'^base_layout', views.base_layout, name='base_layout'),

]
