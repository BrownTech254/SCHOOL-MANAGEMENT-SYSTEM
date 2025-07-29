from django.urls import path
from . import views

urlpatterns = [
	path('lecturer_complete_profile/', views.lecturer_complete_profile, name='lecturer_complete_profile'),
	path('add_lecturer/', views.add_lecturer, name='add_lecturer'),
	path('all_lecturers/', views.all_lecturers, name='all_lecturers'),
]