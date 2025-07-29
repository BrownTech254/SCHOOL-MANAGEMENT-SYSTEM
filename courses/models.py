from django.db import models
from accounts.models import  CustomeUser

# Create your models here.
class Department(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	department_code = models.CharField(max_length=255)
	created_by = models.ForeignKey(CustomeUser, on_delete=models.SET_NULL, null=True, related_name='department')
	modified_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)

	def __str__(self): 
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=255)
	department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='course')
	image = models.ImageField(upload_to='course_images', blank=True, null=True)
	price = models.IntegerField()
	description = models.TextField(blank=True, null=True)
	lecturers = models.ManyToManyField(CustomeUser, related_name='lecturers', blank=True)
	created_by = models.ForeignKey(CustomeUser, on_delete=models.CASCADE, related_name='course')
	modified_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"{self.name} id is {self.id}"
#==============================================================

class CourseLevel(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='levels')
	name = models.CharField(max_length=255, help_text='e.g FirstYear, SecondYear, etc')
	year_number = models.PositiveIntegerField(help_text='e.g 1, 2, etc')
	modified_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)

	class Meta:
		unique_together = ('course', 'year_number')
		ordering = ['year_number']

	def __str__(self):
		return f"{self.name}-{self.course.name}"


class LevelUnit(models.Model):
	level = models.ForeignKey(CourseLevel, on_delete=models.CASCADE, related_name='units')
	name = models.CharField(max_length=255, help_text='e.g communication skills, etc')
	modified_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)

	class Meta:
		unique_together = ('level', 'name')
		ordering = ['-created_at']

	def __str__(self):
		return f"{self.name}-{self.level.course.name}-{self.level.name}"



