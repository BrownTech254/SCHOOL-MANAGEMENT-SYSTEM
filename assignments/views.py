from django.shortcuts import render, redirect
from.models import Assignment, AssignmentSubmission
from .forms import AssignmentForm
from courses.models import Course, CourseLevel, LevelUnit, Department
from django.contrib import messages

# Create your views here.
def all_assignments(request):
	all_assignments = Assignment.objects.all()
	return render(request, 'assignments/all_assignments.html',{
		'all_assignments': all_assignments,
		})

def submissions(request, assignment_id):
	assignment = Assignment.objects.get(id=assignment_id)
	submissions = AssignmentSubmission.objects.filter(assignment=assignment)
	return render(request, 'assignments/submissions.html',{
		'submissions': submissions,
		'assignment': assignment,
		})

def add_assignments(request):
	departments = Department.objects.all()
	form = AssignmentForm()
	if request.method == 'POST':
		unit_id = request.POST.get('unit_id')
		selected_unit = LevelUnit.objects.get(id=unit_id)
		form = AssignmentForm(request.POST, request.FILES)
		if form.is_valid():
			assignment_form = form.save(commit=False)
			assignment_form.unit = selected_unit
			assignment_form.created_by = request.user
			assignment_form.save()
			messages.success(request, 'form submitted successfully')
			return redirect('/dashboard-assignments/all_assignments/')

		else:
			messages.warning(request, 'invalid form ')
			return redirect('/dashboard-assignments/add_assignments/')

	else:
		form = AssignmentForm()


	return render(request, 'assignments/add_assignments.html',{
		'form': form,
		'departments': departments,
		})


def get_courses(request):
	department_id = request.GET.get("department")
	courses = Course.objects.filter(department_id=department_id)
	return render(request, 'assignments/partials/course_select.html', {
		'courses': courses,
		})

def get_levels(request):
	course_id = request.GET.get("course")
	levels = CourseLevel.objects.filter(course_id=course_id)
	return render(request, 'assignments/partials/level_select.html', {
		'levels': levels,
		})

def get_units(request):
	level_id = request.GET.get("level")
	units = LevelUnit.objects.filter(level_id=level_id)
	return render(request, 'assignments/partials/unit_select.html', {
		'units': units,
		})