from django.urls import path
from . import views

urlpatterns = [
	path('add_student/', views.add_student, name='add_student'),
	path('all_students/', views.all_students, name='all_students'),
	path('get-courses/<int:department_id>/', views.get_courses, name='get_courses'),
]