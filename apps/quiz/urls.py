"""trivia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from os import name
from django.contrib.auth import login
from django.urls import path
from . import views
from apps.quiz.views import iniciar, registro, loginView, logout_vista, jugar, resultado_pregunta, ranking


app_name='apps.quiz'

urlpatterns = [
    
    path('registro/', registro, name='registro'),
    path('login/', loginView, name='login'),
    path('iniciar/', iniciar, name='iniciar'),
    path('jugar/', jugar, name='jugar'),
    #path('puntaje/', puntajefinal, name='puntajefinal'),
    path('ranking/', ranking, name='ranking'),
    path('logout_vista/', logout_vista, name='logout_vista'),
    
    
]


