from .base import * 


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'trivia',
        'USER': 'root',
        'PASSWORD': 'clave1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
