from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import get_object_or_404

def index(request):
    return render(request,'tracker/index.html')



from .forms import *

def create_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user  # Asocia el entrenamiento al usuario autenticado
            workout.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()

    return render(request, 'tracker/create_workout.html', {'form': form})

def add_exercise(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout = workout  # Asocia el ejercicio al entrenamiento
            exercise.save()
            return redirect('workout_list')  # Redirige a la lista de entrenamientos
    else:
        form = ExerciseForm()

    return render(request, 'tracker/add_exercise.html', {'form': form, 'workout': workout})







def add_goal(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id, workout__user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.exercise = exercise
            goal.save()
            return redirect('workout_list')  # Cambia a la URL de tu lista de entrenamientos
    else:
        form = GoalForm()

    return render(request, 'tracker/add_goal.html', {'form': form, 'exercise': exercise})




def goal_detail(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, exercise__workout__user=request.user)
    progress_form = ProgressForm()
    progress_data = goal.progress.all().order_by('date')

    if request.method == 'POST' and 'reps_done' in request.POST:
        progress_form = ProgressForm(request.POST)
        if progress_form.is_valid():
            progress = progress_form.save(commit=False)
            progress.goal = goal

            # Validar que las nuevas reps no sean menores al mejor progreso registrado
            max_reps = progress_data.aggregate(max_reps=models.Max('reps_done'))['max_reps'] or 0
            if progress.reps_done < max_reps:
                progress_form.add_error(None, "No puedes retroceder en las repeticiones. Asegúrate de superar o igualar tu último progreso.")
            else:
                progress.save()
                return redirect('goal_detail', goal_id=goal.id)

    # Calcular el progreso basado en el mejor registro
    max_reps = progress_data.aggregate(max_reps=models.Max('reps_done'))['max_reps'] or 0
    target_reps = goal.target_reps or 1
    progress_percentage = min((max_reps / target_reps) * 100, 100)

    return render(request, 'tracker/goal_detail.html', {
        'goal': goal,
        'progress_form': progress_form,
        'progress_data': progress_data,
        'progress_percentage': progress_percentage,
    })











def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'tracker/workout_list.html', {'workouts': workouts})





def competencia(request):
    reto = Reto.objects.filter(user=request.user).latest('created_at')
    picture_gabriel = PictureGabriel.objects.filter(user=request.user).latest('created_at')
    picture_rival = PictureRival.objects.filter(user=request.user).latest('created_at')

    return render(request,'tracker/competencia.html',
                  {'picture_gabriel':picture_gabriel,
                   'picture_rival':picture_rival,
                   'reto':reto})