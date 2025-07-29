from django.urls import path
from .import views

urlpatterns =[
	path('all_departments/', views.all_departments, name='all_departments'),
	path('add_department/', views.add_department, name='add_department'),
	path('add_courses/', views.add_courses, name='add_courses'),
	path('all_courses/', views.all_courses, name='all_courses'),
	path('course_delete/<int:course_id>/', views.course_delete, name='course_delete'),
	path('course_edit/<int:course_id>/', views.course_edit, name='course_edit'),
	path('dept_delete/<int:dept_id>/', views.dept_delete, name='dept_delete'),
	path('dept_edit/<int:dept_id>/', views.dept_edit, name='dept_edit'),
	
]