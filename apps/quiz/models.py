from trivia.settings.base import TIME_ZONE
from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Usuario(models.Model):
    Id_Usuario= primary_key=True 
    Apellido = models.CharField(max_length= 20, null=False, blank=False, help_text="Escriba su Apellido")
    Nombre = models.CharField(max_length= 20, null=False, blank=False, help_text= "Escriba su Nombre")
    Correo = models.EmailField(null=False, blank=False, help_text= "Escriba su correo eléctronico para registrarse y jugar!" )
    Contrasenia = models.CharField(max_length=15, null=False, blank=False, help_text= "Cree una contraseña para completar su registro")
    Nombre_Usuario = models.CharField(max_length=15, null=False, blank=False, help_text= "Elija su nombre con el cual va a jugar!!!")

class Administrador(Usuario):
    Id_Estadisticas= models.ForeignKey('Estadísticas', on_delete=models.CASCADE)
    
class Participante(Usuario):
    Ciudad=  models.CharField(max_length= 25, help_text="Escriba el nombre de su ciudad totalmente en MAYUSCULAS")
    Id_puntaje_general= models.ForeignKey('Puntaje_General', on_delete=models.CASCADE)

class Estadísticas(models.Model):
    Id_Estadisticas= primary_key=True
    Cantidad_Accesos= models.PositiveIntegerField(help_text="Hasta ahora se han logeado en Chaqueña Mente: f{PositiveIntegerField} personas")
    Cantidad_Participantes =models.PositiveIntegerField(help_text="Hasta ahora han jugado Chaqueña Mente: f{PositiveIntegerField} personas")

class Partida(models.Model):
    Id_Partida= primary_key=True
    Id_usuario= models.ForeignKey('Usuario', on_delete=models.CASCADE)
    Puntaje= models.PositiveIntegerField(help_text="Este es su puntaje hasta ahora:")
    Tiempo= models.DurationField(help_text="¡Atención su tiempo va corriendo!")
    Fecha= models.DateTimeField(default=TIME_ZONE)
    Id_puntaje_general= models.ForeignKey('Puntaje_General', on_delete=models.CASCADE)
    Compartir_TW_FB_IG= models.URLField(max_length=500, help_text="Hacé click para compartir tus exitos en tus redes")


class Pregunta(models.Model):
    Id_Pregunta= primary_key=True
    Puntaje =models.PositiveSmallIntegerField
    Correcta= models.BooleanField(True)
    Descripcion = models.CharField(null=False, blank=False, max_length=350, help_text= "Inserte la pregunta")
    Categorias= [('A',	'Cultura y arte'), ('B', 'Historia'), ('C',	'Deporte'), ('D', 'Geografía'), ('E', 'Economía'), ('F', 'Ciencia y Educación'), ('G', 'Entretenimiento')]
    Categoria = models.CharField(choices= Categorias, null=False, max_length=1, help_text= "Elija la categoria de su pregunta elaborada")
    Id_Usuario= models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Respuesta(models.Model):
    Id_Respuesta= primary_key=True
    Correcta= models.BooleanField(True, help_text="Indique cual es la respuesta correcta")
    Descripción = models.CharField(null=False, blank=False, max_length=100, help_text= "Inserte las opciones de respuesta")
    Id_Pregunta= models.ForeignKey('Pregunta', on_delete=models.CASCADE)

class Realiza(models.Model):
    Id_Partida= primary_key=True
    Id_Pregunta= primary_key=True

class Puntaje_General(models.Model):
    Id_puntaje_general= primary_key=True
    Tiempo = models.DurationField
    Por_participante = models.PositiveBigIntegerField
    Por_ciudad = models.PositiveBigIntegerField

    
    


