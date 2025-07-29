from django import forms
from .models import Assignment, AssignmentSubmission

class AssignmentForm(forms.ModelForm):
	class Meta:
		model=Assignment
		fields=['title', 'instruction', 'attachment', 'due_date']
