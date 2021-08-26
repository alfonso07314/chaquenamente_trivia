from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    texto={'mensaje_texto':'Este es mi primer mensaje :)'}
    return render (request, 'index.html',texto)


def contac(request):
    return HttpResponse('hola estoy en la pagina de contacto')
