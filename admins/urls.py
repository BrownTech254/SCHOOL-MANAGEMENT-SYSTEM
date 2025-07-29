from django.urls import path
from .import views

urlpatterns=[
	path('add_admin/', views.add_admin, name='add_admin'),
	path('all_admins/', views.all_admins, name='all_admins'),
	path('admin_complete_profile/', views.admin_complete_profile, name='admin_complete_profile'),
]

