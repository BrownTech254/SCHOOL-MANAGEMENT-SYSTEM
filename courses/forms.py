from django import forms
from .models import Department, Course

class DepartmentForm(forms.ModelForm):
	description = forms.CharField(
		label="Description",
		widget=forms.Textarea(attrs={'row': 4, 'placeholder': 'describe your department'}),
		required=True,
		)

	name = forms.CharField(
		label="Name",
		required=True,
		)

	department_code = forms.CharField(
		label="Department Code",
		required=True,
		)
	class Meta:
		model = Department
		fields = ['name', 'description', 'department_code']

class CourseForm(forms.ModelForm):
	# Styling the department selectbox
	department = forms.ModelChoiceField(
		queryset=Department.objects.all(),
		widget=forms.Select(attrs={'class': 'form-control'}),
		label="Department",
		required=True,
		)

	image = forms.ImageField(
		required = True,
		)

	description = forms.CharField(
		required = True,
		widget=forms.Textarea(attrs={'row': 4}),
		)
	class Meta:
		model=Course
		fields=['name', 'department', 'image', 'price', 'description']
