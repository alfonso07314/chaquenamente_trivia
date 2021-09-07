from django.contrib import admin
from django.contrib.auth.models import User
from apps.quiz.models import Pregunta, Respuesta, PreguntasRespondidas, Partida
from apps.quiz.forms import ElegirInlineFromset

#admin.site.register(Usuario) 
'''Quizas la linea 11 sea innecesaria'''







class ElegirRespuestaInline(admin.TabularInline):
    
    model= Respuesta
    max_num = Respuesta.MAXIMO_RESPUESTA
    min_num = Respuesta.MAXIMO_RESPUESTA
    can_delete = False
    formset = ElegirInlineFromset


class PreguntaAdmin(admin.ModelAdmin):
    model= Pregunta
    inlines = (ElegirRespuestaInline, ) 
    list_display= ['descripcion', ]
    search_fields=[ 'descripcion', 'preguntas__descripcion']


class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display=['pregunta','respuesta','puntaje']
    


admin.site.register(Respuesta)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(PreguntasRespondidas)
admin.site.register(Partida)