from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import DepartmentForm, CourseForm


# Create your views here.
def all_departments(request):
	departments = Department.objects.all()
	return render(request, 'courses/all_department.html', {
		'departments' : departments,
		})

def add_department(request):
	if request.method == "POST":
		form = DepartmentForm(request.POST)
		if form.is_valid():
			dept = form.save(commit=False)
			if Department.objects.filter(name=dept.name, department_code=dept.department_code):
				messages.warning(request, 'department already exists')
				return redirect('/dashboard-departments/add_department/')
			else:				
				dept.created_by = request.user
				dept.save()
				messages.success(request, f'{dept.name} created successfully')
				return redirect('/dashboard-departments/all_departments/')

		else:
			messages.warning(request, 'Error submitting the form')
			return redirect('/dashboard-departments/add_department/')

	else:
		form = DepartmentForm()
	return render(request, 'courses/add_department.html', {
		'form': form,
		})


def add_courses(request):
	if request.method == "POST":
		form = CourseForm(request.POST, request.FILES)#files for files submission
		if form.is_valid():
			course = form.save(commit=False)
			if Course.objects.filter(name=course.name):
				messages.warning(request, 'course already exists')
				return redirect('/dashboard-departments/add_courses/')
			else:				
				course.created_by = request.user
				course.save()
				messages.success(request, f'{course.name} created successfully')
				return redirect('/dashboard-departments/all_courses/')

		else:
			messages.warning(request, 'Error submitting the form')
			return redirect('/dashboard-departments/add_courses/')

	else:
		form = CourseForm()
	return render(request, 'courses/add_course.html', {
		'form': form,
		})
	


	return render(request, 'courses/add_course.html')

def all_courses(request):
	courses = Course.objects.all()
	return render(request, 'courses/all_courses.html', {
		'courses': courses,
		})

def course_delete(request, course_id):
	course = Course.objects.get(id=course_id)
	course.delete()

	messages.success(request, f'{course.name}, deleted successfully')
	return redirect('/dashboard-departments/all_courses/')

def course_edit(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        messages.warning(request, "Course not found.")
        return redirect('/dashboard-departments/all_courses/')

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            new_name = form.cleaned_data.get('name')

            # Check for name conflict, excluding the current course
            if Course.objects.filter(name__iexact=new_name).exclude(id=course.id).exists():
                messages.warning(request, f"A course with the name '{new_name}' already exists.")
                return render(request, 'courses/edit_course.html', {
                    'course': course,
                    'form': form,
                })

            # Save the form
            course_edit = form.save(commit=False)
            course_edit.created_by = request.user
            course_edit.save()

            messages.success(request, f"Course '{course_edit.name}' updated successfully.")
            return redirect('/dashboard-departments/all_courses/')
        else:
            messages.warning(request, 'Error updating the form.')
    else:
        form = CourseForm(instance=course)

    return render(request, 'courses/edit_course.html', {
        'course': course,
        'form': form,
    })

def dept_delete(request, dept_id):
	dept = Department.objects.get(id=dept_id)
	dept.delete()

	messages.success(request, f'{dept.name}, deleted successfully')
	return redirect('/dashboard-departments/all_departments/')

def dept_edit(request, dept_id):
    try:
        dept = Department.objects.get(id=dept_id)
    except Department.DoesNotExist:
        messages.warning(request, "Department not found.")
        return redirect('/dashboard-departments/all_departments/')

    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid():
            new_name = form.cleaned_data.get('name')

            # Check for duplicate department name, excluding the current department
            if Department.objects.filter(name__iexact=new_name).exclude(id=dept.id).exists():
                messages.warning(request, f"A department with the name '{new_name}' already exists.")
                return render(request, 'courses/edit_department.html', {
                    'dept': dept,
                    'form': form,
                })

            department_edit = form.save(commit=False)
            department_edit.created_by = request.user
            department_edit.save()

            messages.success(request, f"Department '{department_edit.name}' updated successfully.")
            return redirect('/dashboard-departments/all_departments/')
        else:
            messages.warning(request, "There was an error with the form.")
            return render(request, 'courses/edit_department.html', {
                'dept': dept,
                'form': form,
            })
    else:
        form = DepartmentForm(instance=dept)

    return render(request, 'courses/edit_department.html', {
        'dept': dept,
        'form': form,
    })
