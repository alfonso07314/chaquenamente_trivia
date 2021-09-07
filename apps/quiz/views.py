''' ------------ GENERAL --------------'''

from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


''' ------------REGISTRO Y LOGUEO USUARIO --------------'''
from apps.quiz.forms import RegistroFormulario, UsuarioLogueoFormulario
from django.contrib.auth import authenticate, login, logout


''' ------------ JUEGO --------------'''
from .models import Partida, Pregunta, PreguntasRespondidas






# Create your views here.
def index(request):
    return render (request, 'index.html')


''' ------------ REGISTRO Y LOGUEO ------------------------ '''


def registro(request):

    titulo = 'crear una cuenta'
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/quiz/login')
    else:
        form= RegistroFormulario()

    context = {

        'form': form,
        'titulo': titulo,
    
    }

    return render(request, 'quiz/registro.html', context)



def loginView(request):
    titulo= 'login'
    form=UsuarioLogueoFormulario(request.POST or None)

    if form.is_valid():
        username= form.cleaned_data.get("username")
        password= form.cleaned_data.get("password")
        usuario= authenticate(username=username , password=password)
        login(request, usuario)
        return redirect('/quiz/iniciar')

    context = {
        'form': form,
        'titulo': titulo
    }

    return render(request, 'quiz/login.html', context)


def logout_vista(request):
    logout(request)
    return redirect('/')

''' ------------ INICIAR ------------------------ '''

def iniciar(request):

    return render(request,'quiz/iniciar.html')



''' ------------ JUGAR ------------------------ '''

def jugar(request):

    

        #CREA  UNA NUEVA PARTIDA
        QuizPartida, created = Partida.objects.get_or_create(participante=request.user)
        
    
        if request.method == 'POST':
            pregunta_pk = request.POST.get('pregunta_pk')
            pregunta_respondida = QuizPartida.intentos.select_related('pregunta').get(pregunta__pk= pregunta_pk) 
            respuesta_pk = request.POST.get('respuesta_pk')

            try:
                opcion_seleccionada = pregunta_respondida.pregunta.opciones.get(pk = respuesta_pk)
            except ObjectDoesNotExist:
                raise Http404


            QuizPartida.validar_intento(pregunta_respondida, opcion_seleccionada)

            cant_preguntasrespondidas= QuizPartida.intentos.count()
            if cant_preguntasrespondidas < 10 :
                return redirect('/quiz/jugar', pregunta_respondida.pk)
            else:
                return redirect('/quiz/ranking')
            

        else:
            pregunta = QuizPartida.obtener_nuevas_preguntas()
            if pregunta is not None:
                QuizPartida.crear_intentos(pregunta)

            context = {

                'pregunta':pregunta
            }

        
        
        return render(request, 'quiz/jugar2.html',context)
          
        

def resultado_pregunta(request, pregunta_respondida_pk):
    respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

    context = {
        'respondida':respondida
    }
    return render(request, 'quiz/resultados.html', context)


''' ------------ RANKING ------------------------ '''

def ranking(request):
    total_partidas_quiz = Partida.objects.order_by('-puntaje_total')[:10]
    contador = total_partidas_quiz.count()
    
    context = {

        'partida_quiz':total_partidas_quiz,
        'contar_partida':contador,
        
    }

    return render(request, 'quiz/ranking.html', context)






