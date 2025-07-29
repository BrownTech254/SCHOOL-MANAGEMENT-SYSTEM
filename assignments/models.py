from django.db import models
from courses.models import LevelUnit
from students.models import Student
from accounts.models import CustomeUser

# Create your models here.
class Assignment(models.Model):
	unit = models.ForeignKey(LevelUnit, on_delete=models.CASCADE, related_name='assignments')
	title = models.CharField(max_length=255)
	instruction = models.TextField()
	created_by = models.ForeignKey(CustomeUser, on_delete=models.SET_NULL, null=True, related_name='assignments')
	attachment = models.FileField(upload_to='assignments', null=True, blank=True)
	due_date = models.DateField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	modified_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.unit}-{self.title}"


class AssignmentSubmission(models.Model):
	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assigments_submitted')
	attachment = models.FileField(upload_to='assignments/submissions', null=True, blank=True)
	is_submitted = models.BooleanField(default=False)
	score = models.IntegerField(help_text='score in percentage(%)', null=True, blank=True)
	grade = models.CharField(help_text='A, B, C, D, etc', null=True, blank=True)
	is_graded = models.BooleanField(default=False)
	submitted_at = models.DateTimeField(blank=True, null=True)
	modified_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.student.user.first_name}--assignment on--{self.assignment.title}"
