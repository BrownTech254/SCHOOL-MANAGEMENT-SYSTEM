from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import CustomeUser
from .models import *
from .forms import *



def lecturer_complete_profile(request):
	logged_in_user = request.user
	logged_in_lecturer, created = Lecturer.objects.get_or_create(user=logged_in_user)

	#pulling all information of the loggged in user
	personal_data, created = Lecturer_Personal_Data.objects.get_or_create(lecturer=logged_in_lecturer)
	family_data, created = Lecturer_Family_Information.objects.get_or_create(lecturer=logged_in_lecturer)
	residence_data, created = Lecturer_Residence.objects.get_or_create(lecturer=logged_in_lecturer)
	emergency_data, created = Lecturer_Emergency_Contact_Persons.objects.get_or_create(lecturer=logged_in_lecturer)
	academic_data, created = Academic_Background.objects.get_or_create(lecturer=logged_in_lecturer)
	
	if request.method == 'POST':
		personal_form = LecturerPersonalDataForm(request.POST, request.FILES, instance=logged_in_lecturer.personal_data if hasattr(logged_in_lecturer, 'personal_data') else None)
		family_form = LecturerFamilyInformationForm(request.POST, instance=logged_in_lecturer.family if hasattr(logged_in_lecturer, 'family') else None)
		residence_form = LecturerResidenceForm(request.POST, instance=logged_in_lecturer.residence if hasattr(logged_in_lecturer, 'residence') else None)
		emergency_form = LecturerEmergencyContactPersonsForm(request.POST, instance=logged_in_lecturer.emergency_contacts if hasattr(logged_in_lecturer, 'emergency_contacts') else None)
		academic_form = AcademicBackgroundForm(request.POST, instance=logged_in_lecturer.academic_data if hasattr(logged_in_lecturer, 'academic_data') else None)

		if all([personal_form.is_valid(), family_form.is_valid(), residence_form.is_valid(), emergency_form.is_valid(), academic_form.is_valid()]):
			personal = personal_form.save(commit=False)
			personal.lecturer = logged_in_lecturer
			personal.save()

			family = family_form.save(commit=False)
			family.lecturer = logged_in_lecturer
			family.save()

			residence = residence_form.save(commit=False)
			residence.lecturer = logged_in_lecturer
			residence.save()

			emergency = emergency_form.save(commit=False)
			emergency.lecturer = logged_in_lecturer
			emergency.save()

			academic = academic_form.save(commit=False)
			academic.lecturer = logged_in_lecturer
			academic.save()

			if not logged_in_lecturer.is_registered:
				logged_in_lecturer.is_registered=True
				logged_in_lecturer.save()

			messages.success(request, 'profile completed succeefully')
			return redirect('/dashboard/teacher_dashboard/')

		else:
			forms_with_errors = {
				'personal data': personal_form,
				'family data': family_form,
				'residenc information': residence_form,
				'emergency info': emergency_form,
				'academic information': academic_form,
			}

			for section_data, form in forms_with_errors.items():
				if not form.is_valid():
					for field, errors in form.errors.items():
						for error in errors:
							messages.warning(request, f'{section_data}-{field}: {error}')
							return redirect('/dashboard/lecturers/lecturer_complete_profile/')



	else:
		personal_form = LecturerPersonalDataForm(instance=personal_data)
		family_form = LecturerFamilyInformationForm(instance=family_data)
		residence_form = LecturerResidenceForm(instance=residence_data)
		emergency_form = LecturerEmergencyContactPersonsForm(instance=emergency_data)
		academic_form = AcademicBackgroundForm(instance=academic_data)


	
	return render(request, 'lecturers/lecturer_complete_profile.html', {
		'personal_form': personal_form,
		'family_form': family_form,
		'residence_form': residence_form,
		'emergency_form': emergency_form,
		'academic_form': academic_form,
		'personal_data': personal_data,
		'family_data': family_data,
		'residence_data': residence_data,
		'emergency_data': emergency_data,
		'academic_data': academic_data,
		})

def add_lecturer(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email_address = request.POST.get('email_address')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')

		if password != confirm_password:
			messages.warning(request, 'passwords did not match')
			return redirect('/dashboard/lecturers/add_lecturer/')

		user = CustomeUser.objects.create_user(first_name=first_name, last_name=last_name, username=email_address, email=email_address, password=password)
		user.is_teacher = True
		user.save()

		lecturer = Lecturer.objects.create(user=user, first_name=first_name, last_name=last_name)
		lecturer.is_registered = False
		lecturer.save()

		messages.success(request, 'Lec added successfully')
		return redirect('/dashboard/lecturers/add_lecturer/')

	return render(request, 'lecturers/add_lecturer.html')


def all_lecturers(request):
	lecturers = Lecturer.objects.all()
	return render(request, 'lecturers/all_lecturers.html', {
		'lecturers': lecturers,
		})

	
