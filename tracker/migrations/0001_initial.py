# Generated by Django 4.2.6 on 2024-11-26 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_del_ejercicio', models.CharField(max_length=255)),
                ('series', models.PositiveIntegerField()),
                ('reps', models.PositiveIntegerField()),
                ('peso', models.FloatField(blank=True, null=True)),
                ('tipo_ejercicio', models.CharField(choices=[('Fuerza', 'Fuerza'), ('Resistencia', 'Resistencia')], max_length=50)),
                ('cronometro', models.PositiveIntegerField(blank=True, help_text='Duración en segundos (opcional)', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Describe la meta del ejercicio', max_length=255)),
                ('target_reps', models.PositiveIntegerField(blank=True, help_text='Repeticiones objetivo (opcional)', null=True)),
                ('target_sets', models.PositiveIntegerField(blank=True, help_text='Series objetivo (opcional)', null=True)),
                ('target_weight', models.FloatField(blank=True, help_text='Peso objetivo (opcional)', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='tracker.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_del_entrenamiento', models.CharField(max_length=255)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps_done', models.PositiveIntegerField(help_text='Repeticiones realizadas')),
                ('date', models.DateField(auto_now_add=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='tracker.goal')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseRM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rm_value', models.PositiveIntegerField()),
                ('exercise', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rm', to='tracker.exercise')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='tracker.workout'),
        ),
    ]
