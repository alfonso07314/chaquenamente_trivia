from django.contrib import admin

# Register your models here.
from apps.quiz.models import Administrador
from apps.quiz.models import Puntaje_General
from apps.quiz.models import Estadísticas

class AdministradorAdmin(admin.ModelAdmin):
    #list_display=("Id_Usuario", "Apellido", "Nombre", "Correo", "Nombre_Usuario")
    search_fields=("Id_Usuario", "Apellido", "Nombre", "Correo", "Nombre_Usuario")
    list_per_page= 10
    pass
admin.site.register(Administrador, AdministradorAdmin)

class EstadisticasAdmin(admin.ModelAdmin):
    #list_display=("Id_Estadisticas", "Cantidad_Accesos", "Cantidad_Participantes")
    search_fields=("Id_Estadisticas", "Cantidad_Accesos", "Cantidad_Participantes")
    list_per_page=25
    pass
admin.site.register(Estadísticas, EstadisticasAdmin)

class Puntaje_GeneralAdmin(admin.ModelAdmin):
    #list_display=("Id_puntaje_general", "Tiempo", "Por_Participante", "Por_Ciudad")
    search_fields=("Id_puntaje_general", "Tiempo", "Por_Participante", "Por_Ciudad")
    list_per_page=25
    #list_max_show_all=("Tiempo", "Por_Participante")
    #list_filter=("Id_puntaje_general", "Tiempo", "Por_Participante", "Por_Ciudad")
    pass
admin.site.register(Puntaje_General, Puntaje_GeneralAdmin)