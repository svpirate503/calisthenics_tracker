from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('crear-entrenamiento/', views.create_workout, name='create_workout'),
    path('workout-list/',views.workout_list,name="workout_list"),
    path('agregar-ejercicio/<int:workout_id>/', views.add_exercise, name='add_exercise'),
    path('agregar-meta/<int:exercise_id>/', views.add_goal, name='add_goal'),
    path('meta-detalle/<int:goal_id>/', views.goal_detail, name='goal_detail'),
    path('competencia/',views.competencia,name='competir')
]
