#from apps.quiz.views import puntaje
from trivia.settings.base import TIME_ZONE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey
import random



# Create your models here.



class Pregunta(models.Model):
    descripcion = models.TextField(null=False, max_length=350, verbose_name= "texto de la pregunta")
    categorias= [('A',	'Cultura y arte'), ('B', 'Historia'), ('C',	'Deporte'), ('D', 'Geografía'), ('E', 'Economía'), ('F', 'Ciencia y Educación'), ('G', 'Entretenimiento')]
    categoria = models.CharField(choices= categorias, default=False, null=False, max_length=1, verbose_name= "Elija la categoria de su pregunta elaborada")
    max_puntaje = models.DecimalField(verbose_name='Maximo Puntaje', default=10, decimal_places=2, max_digits=6)


    NUMERO_DE_RESPUESTAS_PERMITIDAS = 1

    def __str__(self):
        return self.descripcion



class Respuesta(models.Model):

    MAXIMO_RESPUESTA = 4

    correcta= models.BooleanField(default=False, null=False, verbose_name= "marque si es correcta")
    descripcion = models.TextField(null=False, max_length=350, verbose_name= "texto de la respuesta")
    pregunta = ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.descripcion




class Partida(models.Model):
    participante= models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total= models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2,max_digits=10, )

    def crear_intentos(self, pregunta):
        intento = PreguntasRespondidas(pregunta=pregunta , quizParticipante= self)
        intento.save()


    def obtener_nuevas_preguntas(self):
        respondidas = PreguntasRespondidas.objects.filter(quizParticipante=self).values_list('pregunta__pk', flat=True)
        preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        if not preguntas_restantes.exists():
            return None
        return random.choice(preguntas_restantes)


    def validar_intento(self, pregunta_respondida, respuesta_seleccionada):
        if pregunta_respondida.pregunta_id != respuesta_seleccionada.pregunta_id:
            return

        pregunta_respondida.respuesta_seleccionada = respuesta_seleccionada
        if respuesta_seleccionada.correcta is True:
            pregunta_respondida.correcta = True
            pregunta_respondida.puntaje = respuesta_seleccionada.pregunta.max_puntaje
            pregunta_respondida.respuesta = respuesta_seleccionada

        else:
            pregunta_respondida.respuesta = respuesta_seleccionada

        pregunta_respondida.save()

        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        puntaje_actualiado = self.intentos.filter(correcta=True).aggregate(models.Sum('puntaje'))['puntaje__sum']

        self.puntaje_total = puntaje_actualiado
        self.save()

    



class PreguntasRespondidas(models.Model):

    quizParticipante= models.ForeignKey(Partida, on_delete=models.CASCADE, related_name='intentos')
    pregunta= models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta= models.ForeignKey(Respuesta, on_delete=models.CASCADE, null=True)
    correcta= models.BooleanField(verbose_name='Esta es la respuesta correcta?', default=False, null=False)
    puntaje= models.DecimalField(verbose_name='Puntaje Obtenido',default=0, decimal_places= 2, max_digits=6)




