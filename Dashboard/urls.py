from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home2'),
	path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
	path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
	path('profile/', views.profile, name='profile'),
	path('complete_profile/', views.complete_profile, name='complete_profile'),
]