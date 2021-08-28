from django.contrib import admin

# Register your models here.
from django.contrib import admin
from apps.quiz.models import Usuario
from apps.quiz.models import Administrador
from apps.quiz.models import Participante

class Usuario(admin.ModelAdmin):
    pass
admin.site.register(Usuario) 
'''Quizas la linea 11 sea innecesaria'''

class Administrador(admin.ModelAdmin):
    list_display=("Id_Usuario", "Apellido", "Nombre", "Correo", "Nombre_Usuario")
    search_fields=("Id_Usuario", "Apellido", "Nombre", "Correo", "Nombre_Usuario")
    list_per_page= 10
    pass
admin.site.register(Administrador)

class Participante(admin.ModelAdmin):
    list_display=("Id_Usuario", "Apellido", "Nombre", "Correo", "Nombre_Usuario")
    search_fields=("Id_Usuario", "Apellido", "Nombre", "Correo", "Nombre_Usuario")
    list_per_page= 10
    pass
admin.site.register(Participante)

class Estadisticas(admin.ModelAdmin):
    list_display=("Id_Estadisticas", "Cantidad_Accesos", "Cantidad_Participantes")
    search_fields=("Id_Estadisticas", "Cantidad_Accesos", "Cantidad_Participantes")
    list_per_page=25
    pass

class Puntaje_General(admin.ModelAdmin):
    list_display=("Id_puntaje_general", "Tiempo", "Por_Participante", "Por_Ciudad")
    search_fields=("Id_puntaje_general", "Tiempo", "Por_Participante", "Por_Ciudad")
    list_per_page=25
    list_max_show_all=("Tiempo", "Por_Participante")
    list_filter=("Id_puntaje_general", "Tiempo", "Por_Participante", "Por_Ciudad")
    pass