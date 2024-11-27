from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    nombre_del_entrenamiento = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_del_entrenamiento


class Exercise(models.Model):
    TIPO_EJERCICIO_CHOICES = [
        ('Fuerza', 'Fuerza'),
        ('Resistencia', 'Resistencia'),
    ]
    
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    nombre_del_ejercicio = models.CharField(max_length=255)
    series = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    peso = models.FloatField(null=True, blank=True)  # Opcional
    tipo_ejercicio = models.CharField(max_length=50, choices=TIPO_EJERCICIO_CHOICES)
    cronometro = models.PositiveIntegerField(null=True, blank=True, help_text="Duración en segundos (opcional)")

    def registrar_rm(self):
        # Solo registra RM si el ejercicio es 'Pull ups', 'Push ups', o 'Fondos'
        if self.nombre_del_ejercicio.lower() in ['pull ups', 'push ups', 'fondos']:
            return self.reps
        return None

    def __str__(self):
        return f"{self.nombre_del_ejercicio} - {self.workout.nombre_del_entrenamiento}"


class ExerciseRM(models.Model):
    exercise = models.OneToOneField(Exercise, on_delete=models.CASCADE, related_name='rm')
    rm_value = models.PositiveIntegerField()

    def __str__(self):
        return f"RM: {self.rm_value} para {self.exercise.nombre_del_ejercicio}"


class Goal(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='goals')
    description = models.CharField(max_length=255, help_text="Describe la meta del ejercicio")
    target_reps = models.PositiveIntegerField(null=True, blank=True, help_text="Repeticiones objetivo (opcional)")
    target_sets = models.PositiveIntegerField(null=True, blank=True, help_text="Series objetivo (opcional)")
    target_weight = models.FloatField(null=True, blank=True, help_text="Peso objetivo (opcional)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meta para {self.exercise.nombre_del_ejercicio}"


class Progress(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='progress')
    reps_done = models.PositiveIntegerField(help_text="Repeticiones realizadas")
    date = models.DateField(auto_now_add=True)

    def clean(self):
        # Obtener el último progreso registrado para esta meta
        last_progress = Progress.objects.filter(goal_id=self.goal_id).order_by('-date').first()
        if last_progress and self.reps_done < last_progress.reps_done:
            raise ValidationError("No puedes retroceder en las repeticiones. Asegúrate de superar o igualar tu último progreso.")

    def save(self, *args, **kwargs):
        self.clean()  # Llamar a la validación antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reps_done} reps el {self.date} para {self.goal}"
    



class PictureGabriel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures')
    created_at = models.DateTimeField(auto_now_add=True)



class PictureRival(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures')
    created_at = models.DateTimeField(auto_now_add=True)

class Reto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.name