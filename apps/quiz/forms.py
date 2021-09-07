

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from apps.quiz.models import Pregunta , Respuesta, PreguntasRespondidas






""" ------------------ NO PERMITIR QUE EL ADMINISTRADOR SELECCIONE MAS DE UNA RESPUESTA CORRECTA --------------------------- """

class ElegirInlineFromset(forms.BaseInlineFormSet):
 
    def clean(self):
        super(ElegirInlineFromset, self).clean()

        respuesta_correcta = 0
        for formulario in self.forms:
            if not formulario.is_valid():
                return

            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuesta_correcta += 1

        
        try:
            
            assert respuesta_correcta == Pregunta.NUMERO_DE_RESPUESTAS_PERMITIDAS

        except AssertionError:
            raise forms.ValidationError('Solo una respueta puede ser correcta')




""" ------------------ REGISTRO --------------------------- """

User= get_user_model()

class RegistroFormulario(UserCreationForm):

    email=forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = User

        fields = [

            'username',
            'email',
            'password1',
            'password2'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),

        }



""" ------------------ LOGUEO --------------------------- """


class UsuarioLogueoFormulario(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs ):
        username= self.cleaned_data.get('username')
        password= self.cleaned_data.get('password')

        if username and password:

            user= authenticate(username=username , password= password)
        
            if not user:
                raise forms.ValidationError("Este usuario no existe")
        
            if not user.check_password(password):
                raise forms.ValidationError("Contraseña Incorrecta")

            if not user.is_active:
                raise forms.ValidationError("Este usuario NO esta activo")

        return super(UsuarioLogueoFormulario, self).clean(*args, **kwargs)
        
    
