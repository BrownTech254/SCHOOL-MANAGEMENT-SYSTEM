from django.urls import path
from . import views

urlpatterns = [
	path('signin/', views.user_login, name='user_login'),
	path('signout/', views.user_logout, name='user_logout'),
]