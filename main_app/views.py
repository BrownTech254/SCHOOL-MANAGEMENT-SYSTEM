from django.shortcuts import render, redirect
from courses.models import Course
from accounts.models import CustomeUser
from django.contrib import messages
from students.models import Student

def home(request):
	return render(request, 'main_app/home.html')

def courses(request):
	courses = Course.objects.all()
	return render(request, 'main_app/courses.html', {
 		'courses': courses,
 		})


	

def course_enrollment(request, course_id):
	course = Course.objects.get(id=course_id)
	if request.method == "POST":
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		email = request.POST.get("email")
		password1 = request.POST.get("password1")
		password2 = request.POST.get("password2")

		if password1 != password2:
			messages.warning(request, 'your password did not match')
			return redirect(f'/course_enrollment/{course.id}/')

		user = CustomeUser.objects.create_user(username=first_name, first_name=first_name, last_name=last_name, email=email, password=password1)
		user.is_student = True
		user.save()

		student = Student.objects.create(user=user, first_name=first_name, last_name=last_name, course=course)
		student.is_registered = False
		student.save()

		messages.success(request, 'successsfully creation')
		return redirect('/accounts/signin/')




	return render(request, 'main_app/course_enrollment.html', {
		'course':course,
		})
 
def course_details(request, course_id):
	
	course = Course.objects.get(id=course_id)
	return render(request, 'main_app/course_details.html', {
		'course':course,
		})
 	