# Generated by Django 3.0 on 2021-09-03 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntasRespondidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='Esta es la respuesta correcta?')),
                ('puntaje', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Puntaje Obtenido')),
            ],
        ),
        migrations.RemoveField(
            model_name='partida',
            name='correcta',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='pregunta',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='puntaje',
        ),
        migrations.RemoveField(
            model_name='partida',
            name='respuesta',
        ),
        migrations.AddField(
            model_name='partida',
            name='puntaje_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Puntaje Total'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='max_puntaje',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=6, verbose_name='Maximo Puntaje'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='participante',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opciones', to='quiz.Pregunta'),
        ),
        migrations.DeleteModel(
            name='Participante',
        ),
        migrations.AddField(
            model_name='preguntasrespondidas',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Pregunta'),
        ),
        migrations.AddField(
            model_name='preguntasrespondidas',
            name='quizParticipante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='quiz.Partida'),
        ),
        migrations.AddField(
            model_name='preguntasrespondidas',
            name='respuesta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Respuesta'),
        ),
    ]
