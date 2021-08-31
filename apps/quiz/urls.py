from django.urls import path
from . import views

app_name='apps.quiz'

urlpatterns = [
    
    path('iniciar', views.iniciar, name='iniciar'),
    path('play', views.play, name='play'),
    path('puntaje', views.puntaje, name='puntaje'),
    
    

]