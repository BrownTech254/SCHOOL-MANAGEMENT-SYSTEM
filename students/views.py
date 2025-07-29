from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from accounts.models import CustomeUser
from .models import *
from courses.models import Department, Course

def get_courses(request, department_id):
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)

def add_student(request):
	departments = Department.objects.all()
	if request.method == 'POST':
		course_id = request.POST.get('course_id')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email_address = request.POST.get('email_address')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')

		course = Course.objects.get(id=course_id)
		print(f"{course.name}")

		if CustomeUser.objects.filter(username=email_address, email=email_address):
			messages.warning(request, 'email already exists')
			return redirect('/dashboard-students/add_student/')

		if password != confirm_password:
			messages.warning(request, 'Check your password and try again')
			return redirect('/dashboard-students/add_student/')

		user = CustomeUser.objects.create_user(first_name=first_name, last_name=last_name, email=email_address, password=password, username=email_address)
		user.is_student = True
		user.save()

		student = Student.objects.create(user=user, first_name=first_name, last_name=last_name, course=course)
		student.is_registered = False
		student.save()

		messages.success(request, f' {first_name} added successfully to {course.name}')
		return redirect('/dashboard-students/add_student/')

	return render(request, 'students/add_student.html', {
		'departments': departments,
		})
def all_students(request):
	students = Student.objects.all()
	return render(request, 'students/all_students.html', {
		'students' : students
		})





