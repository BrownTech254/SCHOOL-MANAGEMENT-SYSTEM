from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomeUser(AbstractUser):
	is_admin = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	is_student = models.BooleanField(default=False)


	def __str__(self):
		return self.username

