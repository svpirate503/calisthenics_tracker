from django.contrib import admin
from .models import *

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('nombre_del_entrenamiento', 'user', 'fecha_creacion')
    search_fields = ('nombre_del_entrenamiento', 'user__username')

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('nombre_del_ejercicio', 'workout', 'tipo_ejercicio', 'series', 'reps', 'peso', 'cronometro')
    list_filter = ('tipo_ejercicio',)
    search_fields = ('nombre_del_ejercicio', 'workout__nombre_del_entrenamiento')

@admin.register(ExerciseRM)
class ExerciseRMAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'rm_value')
admin.site.register(Goal)
admin.site.register(Progress)
admin.site.register(PictureGabriel)
admin.site.register(PictureRival)
admin.site.register(Reto)