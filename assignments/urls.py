from django.urls import path
from .import views

urlpatterns =[
	path('all_assignments/', views.all_assignments, name='all_assignments'),
	path('add_assignments/', views.add_assignments, name='add_assignments'),
	path('submissions/<int:assignment_id>/', views.submissions, name='submissions'),
	path('get_courses/', views.get_courses, name='get_courses'),
	path('get_levels/', views.get_levels, name='get_levels'),
	path('get_units/', views.get_units, name='get_units'),

	
]