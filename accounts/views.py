from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def user_login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			if request.user.is_admin:
				messages.success(request, 'welcome back')
				return redirect('/dashboard/')
			elif request.user.is_teacher:
				messages.success(request, 'welcome back')
				return redirect('/dashboard/teacher_dashboard/')
			elif request.user.is_student:
				messages.success(request, 'welcome back')
				return redirect('/dashboard/student_dashboard/')
			else:
				messages.warning(request, 'please contact your system admin for further assistance')
				return redirect('/accounts/signin/')
			
		else:
			messages.warning(request, 'Invalid username or password. Please check your credentials and try again.')
			messages.info(request, 'New here? Consider enrolling to create an account.')
			return redirect('/accounts/signin/')
	return render(request, 'accounts/login.html')

def user_logout(request):
	logout(request)
	messages.success(request, 'logout successful')
	return redirect('/accounts/signin/')