from django.urls import path
from . import views

app_name='apps.quiz'

urlpatterns = [
    path('contacto', views.contac, name='contac'),
]