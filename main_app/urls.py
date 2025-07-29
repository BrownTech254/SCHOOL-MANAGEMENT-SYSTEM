from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('courses/', views.courses, name='courses'),
	path('course_enrollment/<int:course_id>/', views.course_enrollment, name='course_enrollment'),
	path('course_details/<int:course_id>/', views.course_details, name='course_details'),
]