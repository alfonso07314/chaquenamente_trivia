from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request, 'index.html')


def iniciar(request):
    return render (request, 'quiz/iniciar.html')

def play(request):
    return render (request, 'quiz/juego.html')


def puntaje(request):
    return render (request, 'quiz/puntaje.html')











