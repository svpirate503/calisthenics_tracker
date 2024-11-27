from django import forms
from .models import Workout,Goal,Progress

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['nombre_del_entrenamiento']
        widgets = {
            'nombre_del_entrenamiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del entrenamiento'}),
        }
from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['nombre_del_ejercicio', 'series', 'reps', 'peso', 'tipo_ejercicio', 'cronometro']
        widgets = {
            'nombre_del_ejercicio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del ejercicio'}),
            'series': forms.NumberInput(attrs={'class': 'form-control'}),
            'reps': forms.NumberInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Opcional'}),
            'tipo_ejercicio': forms.Select(attrs={'class': 'form-control'}),
            'cronometro': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'En segundos (Opcional)'}),
        }




class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['description', 'target_reps', 'target_sets', 'target_weight']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describe la meta'}),
            'target_reps': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Repeticiones (opcional)'}),
            'target_sets': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Series (opcional)'}),
            'target_weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso (opcional)'}),
        }




class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['reps_done']
        widgets = {
            'reps_done': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '¿Cuántas reps hiciste hoy?'}),
        }