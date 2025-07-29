from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import CustomeUser
from .models import *
from .forms import *

# Create your views here.
def add_admin(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email_address = request.POST.get('email_address')
		password= request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')

		if password != confirm_password:
			messages.warning(request, 'Check your password')
			return redirect('/dashboard/admins/add_admin/')

		user = CustomeUser.objects.create_user(first_name=first_name, last_name=last_name, username=email_address, email=email_address, password=password)
		user.is_admin = True
		user.save()	

		admin = Admin.objects.create(user=user, first_name=last_name, last_name=last_name)
		admin.is_registered = False
		admin.save()

		messages.success(request, 'Admin added successfully')
		return redirect('/dashboard/admins/add_admin/')

	return render(request, 'admins/add_admin.html')

def all_admins(request):
	admins = Admin.objects.all()
	return render(request, 'admins/all_admins.html', {
		'admins': admins,
		})

def admin_complete_profile(request):
	logged_in_user = request.user
	logged_in_admin, created = Admin.objects.get_or_create(user=logged_in_user)

	#pulling all information of the loggged in user
	personal_data, created = Admin_Personal_Data.objects.get_or_create(admin=logged_in_admin)
	family_data, created = Admin_Family_Information.objects.get_or_create(admin=logged_in_admin)
	residence_data, created = Admin_Residence.objects.get_or_create(admin=logged_in_admin)
	emergency_data, created = Admin_Emergency_Contact_Persons.objects.get_or_create(admin=logged_in_admin)
	academic_data, created = Academic_Background.objects.get_or_create(admin=logged_in_admin)
	
	if request.method == 'POST':
		personal_form = AdminPersonalDataForm(request.POST, request.FILES, instance=logged_in_admin.personal_data if hasattr(logged_in_admin, 'personal_data') else None)
		family_form = AdminFamilyInformationForm(request.POST, instance=logged_in_admin.family if hasattr(logged_in_admin, 'family') else None)
		residence_form = AdminResidenceForm(request.POST, instance=logged_in_admin.residence if hasattr(logged_in_admin, 'residence') else None)
		emergency_form = AdminEmergencyContactPersonsForm(request.POST, instance=logged_in_admin.emergency_contacts if hasattr(logged_in_admin, 'emergency_contacts') else None)
		academic_form = AcademicBackgroundForm(request.POST, instance=logged_in_admin.academic_data if hasattr(logged_in_admin, 'academic_data') else None)

		if all([personal_form.is_valid(), family_form.is_valid(), residence_form.is_valid(), emergency_form.is_valid(), academic_form.is_valid()]):
			personal = personal_form.save(commit=False)
			personal.admin = logged_in_admin
			personal.save()

			family = family_form.save(commit=False)
			family.admin = logged_in_admin
			family.save()

			residence = residence_form.save(commit=False)
			residence.admin = logged_in_admin
			residence.save()

			emergency = emergency_form.save(commit=False)
			emergency.admin = logged_in_admin
			emergency.save()

			academic = academic_form.save(commit=False)
			academic.admin = logged_in_admin
			academic.save()

			if not logged_in_admin.is_registered:
				logged_in_admin.is_registered=True
				logged_in_admin.save()

			messages.success(request, 'profile completed succeefully')
			return redirect('/dashboard/')

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
							return redirect('/dashboard/admins/admin_complete_profile/')



	else:
		personal_form = AdminPersonalDataForm(instance=personal_data)
		family_form = AdminFamilyInformationForm(instance=family_data)
		residence_form = AdminResidenceForm(instance=residence_data)
		emergency_form = AdminEmergencyContactPersonsForm(instance=emergency_data)
		academic_form = AcademicBackgroundForm(instance=academic_data)


	
	return render(request, 'admins/admin_complete_profile.html', {
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