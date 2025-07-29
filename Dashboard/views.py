from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from students.countries import NATIONALITY_CHOICES
from students.counties import COUNTY_CHOICES
from students.models import *
from django.contrib.auth.decorators import login_required
from courses.models import CourseLevel

@login_required
def home(request):
    if not request.user.is_admin:
        logout(request)
        return redirect('/accounts/signin/')
    return render(request, 'Dashboard/home.html')

@login_required
def teacher_dashboard(request):
    if not request.user.is_teacher:
        logout(request)
        return redirect('/accounts/signin/')
    return render(request, 'Dashboard/teacher_dashboard.html')

@login_required
def student_dashboard(request):
    if not request.user.is_student:
        logout(request)
        return redirect('/accounts/signin/')
    return render(request, 'Dashboard/student_dashboard.html')

@login_required
def profile(request):
	return render(request, 'Dashboard/profile.html')
	

@login_required
def complete_profile(request):
    if not request.user.is_student:
        logout(request)
        return redirect('/accounts/signin/')
        
    student, created = Student.objects.get_or_create(user=request.user)  # allows authenticated users to view their own profile
    student_course = student.course.name
    student_course_levels = CourseLevel.objects.filter(course=student.course)
    if request.user.student.is_registered:
        return redirect('/dashboard/student_dashboard/')

    # Getting all the information for the logged-in student or create if there is none
    # we unpack the models to avoid saving errors
    personal_data, created = Student_Personal_Data.objects.get_or_create(student=student)
    family_information, created = Student_Family_Information.objects.get_or_create(student=student)
    residence, created = Student_Residence.objects.get_or_create(student=student)
    emergency_contacts, created = Student_Emergency_Contact_Persons.objects.get_or_create(student=student)
    academic_background, created = Academic_Background.objects.get_or_create(student=student)

    # Getting data from our HTML form in the frontend
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        level_id = request.POST.get('level_id')
        passport_image = request.FILES.get('passport_image')
        national_id = request.POST.get('national_id')
        huduma_number = request.POST.get('huduma_number')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')
        name_of_spouse_if_married = request.POST.get('name_of_spouse_if_married')
        number_of_children_if_married = request.POST.get('number_of_children_if_married')
        occupation_of_spouse_if_married = request.POST.get('occupation_of_spouse_if_married')
        phone_number_of_spouse_if_married = request.POST.get('phone_number_of_spouse_if_married')
        physical_impairement = request.POST.get('physical_impairement')
        if_physical_impairment = request.POST.get('if_physical_impairment')
        nhif_number = request.POST.get('nhif_number')
        religion = request.POST.get('religion')
        nationality = request.POST.get('nationality')
        phone_number = request.POST.get('phone_number')
        postal_box = request.POST.get('postal_box')
        postal_code = request.POST.get('postal_code')
        postal_town = request.POST.get('postal_town')

        # Getting family data
        father_first_name = request.POST.get('father_first_name')
        father_last_name = request.POST.get('father_last_name')
        father_status = request.POST.get('father_status')
        father_occupation = request.POST.get('father_occupation')
        father_date_of_birth = request.POST.get('father_date_of_birth')

        mother_first_name = request.POST.get('mother_first_name')
        mother_last_name = request.POST.get('mother_last_name')
        mother_status = request.POST.get('mother_status')
        mother_occupation = request.POST.get('mother_occupation')
        mother_date_of_birth = request.POST.get('mother_date_of_birth')

        number_of_brothers_and_sisters = request.POST.get('number_of_brothers_and_sisters')

        # Getting residence
        place_of_birth = request.POST.get('place_of_birth')
        place_of_permanent_residence = request.POST.get('place_of_permanent_residence')
        nearest_town = request.POST.get('nearest_town')
        location = request.POST.get('location')
        name_of_chief = request.POST.get('name_of_chief')
        county = request.POST.get('county')
        sub_county = request.POST.get('sub_county')
        constituency = request.POST.get('constituency')
        nearest_police_station = request.POST.get('nearest_police_station')

        # Getting emergency contacts
        # Contact Person A
        first_name_a = request.POST.get('first_name_a')
        last_name_a = request.POST.get('last_name_a')
        email_a = request.POST.get('email_a')
        phone_number_a = request.POST.get('phone_number_a')
        postal_box_a = request.POST.get('postal_box_a')
        postal_code_a = request.POST.get('postal_code_a')
        postal_town_a = request.POST.get('postal_town_a')
        relationship_a = request.POST.get('relationship_a')

        # Contact Person B
        first_name_b = request.POST.get('first_name_b')
        last_name_b = request.POST.get('last_name_b')
        email_b = request.POST.get('email_b')
        phone_number_b = request.POST.get('phone_number_b')
        postal_box_b = request.POST.get('postal_box_b')
        postal_code_b = request.POST.get('postal_code_b')
        postal_town_b = request.POST.get('postal_town_b')
        relationship_b = request.POST.get('relationship_b')

        # Academic 
        name_of_secondary_school = request.POST.get('name_of_secondary_school')
        index_number_of_secondary_school = request.POST.get('index_number_of_secondary_school')
        year_of_completion_of_secondary_school = request.POST.get('year_of_completion_of_secondary_school')

        name_of_primary_school = request.POST.get('name_of_primary_school')
        index_number_of_primary_school = request.POST.get('index_number_of_primary_school')
        year_of_completion_of_primary_school = request.POST.get('year_of_completion_of_primary_school')

        kcpe_results = request.POST.get('kcpe_results')
        any_other_institution_atttended_and_qualifications_attained = request.POST.get('any_other_institution_atttended_and_qualifications_attained')

        # Before Saving We want to provide checks for the data posted by the user and
        # also define required fields 

        if not first_name or first_name == "None":
            messages.warning(request, "You should provide your first name")
            return redirect('/dashboard/complete_profile/')

        if not last_name or last_name == "None":
            messages.warning(request, "You should provide your last name")
            return redirect('/dashboard/complete_profile/')

        if not email or email == "None":
            messages.warning(request, "You should provide an email address")
            return redirect('/dashboard/complete_profile/')

        if not passport_image:
            messages.warning(request, "You should upload a passport image")
            return redirect('/dashboard/complete_profile/')

        if not national_id or national_id == "None":
            messages.warning(request, "You should provide your national ID")
            return redirect('/dashboard/complete_profile/')

        
        if not date_of_birth or date_of_birth == "None":
            messages.warning(request, "You should provide your date of birth")
            return redirect('/dashboard/complete_profile/')

        if not gender or gender == "None":
            messages.warning(request, "You should select your gender")
            return redirect('/dashboard/complete_profile/')

        if not marital_status or marital_status == "None":
            messages.warning(request, "You should select your marital status")
            return redirect('/dashboard/complete_profile/')

        if marital_status == "Married":
            if not name_of_spouse_if_married or name_of_spouse_if_married == "None":
                messages.warning(request, "You should provide your spouse's name")
                return redirect('/dashboard/complete_profile/')

            if not name_of_spouse_if_married or name_of_spouse_if_married == "None":
                messages.warning(request, "You should provide your spouse's name")
                return redirect('/dashboard/complete_profile/')

            if not number_of_children_if_married or number_of_children_if_married == "None":
                messages.warning(request, "You should provide number of children")
                return redirect('/dashboard/complete_profile/')

            if number_of_children and number_of_children.strip().isdigit():
                number_of_children = int(number_of_children)
            else:
                number_of_children = 0  # or None, depending on your model setup

            if not occupation_of_spouse_if_married or occupation_of_spouse_if_married == "None":
                messages.warning(request, "You should provide your spouse's occupation")
                return redirect('/dashboard/complete_profile/')

            if not phone_number_of_spouse_if_married or phone_number_of_spouse_if_married == "None":
                messages.warning(request, "You should provide your spouse's phone number")
                return redirect('/dashboard/complete_profile/')        

        if not physical_impairement or physical_impairement == "None":
            messages.warning(request, "You should indicate physical impairment")
            return redirect('/dashboard/complete_profile/')

        if physical_impairement == "Yes":
            if not if_physical_impairment or if_physical_impairment == "None":
                messages.warning(request, "You should describe your physical impairment")
                return redirect('/dashboard/complete_profile/')

        
        if not religion or religion == "None":
            messages.warning(request, "You should select your religion")
            return redirect('/dashboard/complete_profile/')

        if not nationality or nationality == "None":
            messages.warning(request, "You should select your nationality")
            return redirect('/dashboard/complete_profile/')

        if not phone_number or phone_number == "None":
            messages.warning(request, "You should provide your phone number")
            return redirect('/dashboard/complete_profile/')

        if not postal_box or postal_box == "None":
            messages.warning(request, "You should provide your postal box")
            return redirect('/dashboard/complete_profile/')

        if not postal_code or postal_code == "None":
            messages.warning(request, "You should provide your postal code")
            return redirect('/dashboard/complete_profile/')

        if not postal_town or postal_town == "None":
            messages.warning(request, "You should provide your postal town")
            return redirect('/dashboard/complete_profile/')

        if not father_first_name or father_first_name == "None":
            messages.warning(request, "You should provide your father's first name")
            return redirect('/dashboard/complete_profile/')

        if not father_last_name or father_last_name == "None":
            messages.warning(request, "You should provide your father's last name")
            return redirect('/dashboard/complete_profile/')

        if not father_status or father_status == "None":
            messages.warning(request, "You should indicate your father's status")
            return redirect('/dashboard/complete_profile/')

        if not father_occupation or father_occupation == "None":
            messages.warning(request, "You should provide your father's occupation")
            return redirect('/dashboard/complete_profile/')

        if not father_date_of_birth or father_date_of_birth == "None":
            messages.warning(request, "You should provide your father's date of birth")
            return redirect('/dashboard/complete_profile/')

        if not mother_first_name or mother_first_name == "None":
            messages.warning(request, "You should provide your mother's first name")
            return redirect('/dashboard/complete_profile/')

        if not mother_last_name or mother_last_name == "None":
            messages.warning(request, "You should provide your mother's last name")
            return redirect('/dashboard/complete_profile/')

        if not mother_status or mother_status == "None":
            messages.warning(request, "You should indicate your mother's status")
            return redirect('/dashboard/complete_profile/')

        if not mother_occupation or mother_occupation == "None":
            messages.warning(request, "You should provide your mother's occupation")
            return redirect('/dashboard/complete_profile/')

        if not mother_date_of_birth or mother_date_of_birth == "None":
            messages.warning(request, "You should provide your mother's date of birth")
            return redirect('/dashboard/complete_profile/')

        if not number_of_brothers_and_sisters or number_of_brothers_and_sisters == "None":
            messages.warning(request, "You should provide the number of brothers and sisters")
            return redirect('/dashboard/complete_profile/')

        if number_of_brothers_and_sisters and number_of_brothers_and_sisters.strip().isdigit():
            number_of_brothers_and_sisters = int(number_of_brothers_and_sisters)
        else:
            number_of_brothers_and_sisters = 0  # 

        if not place_of_birth or place_of_birth == "None":
            messages.warning(request, "You should provide your place of birth")
            return redirect('/dashboard/complete_profile/')

        if not place_of_permanent_residence or place_of_permanent_residence == "None":
            messages.warning(request, "You should provide your place of permanent residence")
            return redirect('/dashboard/complete_profile/')

        if not nearest_town or nearest_town == "None":
            messages.warning(request, "You should provide your nearest town")
            return redirect('/dashboard/complete_profile/')

        if not location or location == "None":
            messages.warning(request, "You should provide your location")
            return redirect('/dashboard/complete_profile/')

        if not name_of_chief or name_of_chief == "None":
            messages.warning(request, "You should provide the name of your chief")
            return redirect('/dashboard/complete_profile/')

        if not county or county == "None":
            messages.warning(request, "You should provide your county")
            return redirect('/dashboard/complete_profile/')

        if not sub_county or sub_county == "None":
            messages.warning(request, "You should provide your sub-county")
            return redirect('/dashboard/complete_profile/')

        if not constituency or constituency == "None":
            messages.warning(request, "You should provide your constituency")
            return redirect('/dashboard/complete_profile/')

        if not nearest_police_station or nearest_police_station == "None":
            messages.warning(request, "You should provide your nearest police station")
            return redirect('/dashboard/complete_profile/')

        # Contact Person A
        if not first_name_a or first_name_a == "None":
            messages.warning(request, "You should provide the first name of emergency contact person A")
            return redirect('/dashboard/complete_profile/')

        if not last_name_a or last_name_a == "None":
            messages.warning(request, "You should provide the last name of emergency contact person A")
            return redirect('/dashboard/complete_profile/')

        if not email_a or email_a == "None":
            messages.warning(request, "You should provide the email of emergency contact person A")
            return redirect('/dashboard/complete_profile/')

        if not phone_number_a or phone_number_a == "None":
            messages.warning(request, "You should provide the phone number of emergency contact person A")
            return redirect('/dashboard/complete_profile/')

        if not postal_box_a or postal_box_a == "None":
            messages.warning(request, "You should provide the postal box of emergency contact person A")
            return redirect('/dashboard/complete_profile/')

        if not postal_code_a or postal_code_a == "None":
            messages.warning(request, "You should provide the postal code of emergency contact person A")
            return redirect('/dashboard/complete_profile/')

        if not postal_town_a or postal_town_a == "None":
            messages.warning(request, "You should provide the postal town of emergency contact person A")
            return redirect('/dashboard/complete_profile/')

        if not relationship_a or relationship_a == "None":
            messages.warning(request, "You should provide the relationship of emergency contact person A")
            return redirect('/dashboard/complete_profile/')

        # Contact Person B
        if not first_name_b or first_name_b == "None":
            messages.warning(request, "You should provide the first name of emergency contact person B")
            return redirect('/dashboard/complete_profile/')

        if not last_name_b or last_name_b == "None":
            messages.warning(request, "You should provide the last name of emergency contact person B")
            return redirect('/dashboard/complete_profile/')

        if not email_b or email_b == "None":
            messages.warning(request, "You should provide the email of emergency contact person B")
            return redirect('/dashboard/complete_profile/')

        if not phone_number_b or phone_number_b == "None":
            messages.warning(request, "You should provide the phone number of emergency contact person B")
            return redirect('/dashboard/complete_profile/')

        if not postal_box_b or postal_box_b == "None":
            messages.warning(request, "You should provide the postal box of emergency contact person B")
            return redirect('/dashboard/complete_profile/')

        if not postal_code_b or postal_code_b == "None":
            messages.warning(request, "You should provide the postal code of emergency contact person B")
            return redirect('/dashboard/complete_profile/')

        if not postal_town_b or postal_town_b == "None":
            messages.warning(request, "You should provide the postal town of emergency contact person B")
            return redirect('/dashboard/complete_profile/')

        if not relationship_b or relationship_b == "None":
            messages.warning(request, "You should provide the relationship of emergency contact person B")
            return redirect('/dashboard/complete_profile/')

        # Academic Background
        if not name_of_secondary_school or name_of_secondary_school == "None":
            messages.warning(request, "You should provide the name of your secondary school")
            return redirect('/dashboard/complete_profile/')

        if not index_number_of_secondary_school or index_number_of_secondary_school == "None":
            messages.warning(request, "You should provide your secondary school index number")
            return redirect('/dashboard/complete_profile/')

        if index_number_of_secondary_school and index_number_of_secondary_school.strip().isdigit():
            index_number_of_secondary_school = int(index_number_of_secondary_school)
        else:
            index_number_of_secondary_school = 0  # 

        if not year_of_completion_of_secondary_school or year_of_completion_of_secondary_school == "None":
            messages.warning(request, "You should provide the year you completed secondary school")
            return redirect('/dashboard/complete_profile/')

        if not name_of_primary_school or name_of_primary_school == "None":
            messages.warning(request, "You should provide the name of your primary school")
            return redirect('/dashboard/complete_profile/')

        if not index_number_of_primary_school or index_number_of_primary_school == "None":
            messages.warning(request, "You should provide your primary school index number")
            return redirect('/dashboard/complete_profile/')

        if not year_of_completion_of_primary_school or year_of_completion_of_primary_school == "None":
            messages.warning(request, "You should provide the year you completed primary school")
            return redirect('/dashboard/complete_profile/')

        if index_number_of_primary_school and index_number_of_primary_school.strip().isdigit():
            index_number_of_primary_school = int(index_number_of_primary_school)
        else:
            index_number_of_primary_school = 0  # 

        if not kcpe_results or kcpe_results == "None":
            messages.warning(request, "You should provide your KCPE results")
            return redirect('/dashboard/complete_profile/')

        if not any_other_institution_atttended_and_qualifications_attained or any_other_institution_atttended_and_qualifications_attained == "None":
            messages.warning(request, "You should provide any other institution attended and qualifications attained")
            return redirect('/dashboard/complete_profile/')

        # Now save all the data to the database

        # Save Personal Data
        personal_data.first_name = first_name
        personal_data.last_name = last_name
        personal_data.email = email
        if passport_image:
            personal_data.passport_image = passport_image
        personal_data.national_id = national_id
        personal_data.huduma_number = huduma_number
        personal_data.date_of_birth = date_of_birth
        personal_data.gender = gender
        personal_data.marital_status = marital_status
        personal_data.name_of_spouse_if_married = name_of_spouse_if_married
        personal_data.number_of_children_if_married = number_of_children_if_married
        personal_data.occupation_of_spouse_if_married = occupation_of_spouse_if_married
        personal_data.phone_number_of_spouse_if_married = phone_number_of_spouse_if_married
        personal_data.physical_impairement = physical_impairement
        personal_data.if_physical_impairment = if_physical_impairment
        personal_data.nhif_number = nhif_number
        personal_data.religion = religion
        personal_data.nationality = nationality
        personal_data.phone_number = phone_number
        personal_data.postal_box = postal_box
        personal_data.postal_code = postal_code
        personal_data.postal_town = postal_town
        personal_data.save()

        # Save Family Information
        family_information.father_first_name = father_first_name
        family_information.father_last_name = father_last_name
        family_information.father_status = father_status
        family_information.father_occupation = father_occupation
        family_information.father_date_of_birth = father_date_of_birth
        family_information.mother_first_name = mother_first_name
        family_information.mother_last_name = mother_last_name
        family_information.mother_status = mother_status
        family_information.mother_occupation = mother_occupation
        family_information.mother_date_of_birth = mother_date_of_birth
        family_information.number_of_brothers_and_sisters = number_of_brothers_and_sisters
        family_information.save()

        # Save Residence Information
        residence.place_of_birth = place_of_birth
        residence.place_of_permanent_residence = place_of_permanent_residence
        residence.nearest_town = nearest_town
        residence.location = location
        residence.name_of_chief = name_of_chief
        residence.county = county
        residence.sub_county = sub_county
        residence.constituency = constituency
        residence.nearest_police_station = nearest_police_station
        residence.save()

        # Save Emergency Contacts
        emergency_contacts.first_name_a = first_name_a
        emergency_contacts.last_name_a = last_name_a
        emergency_contacts.email_a = email_a
        emergency_contacts.phone_number_a = phone_number_a
        emergency_contacts.postal_box_a = postal_box_a
        emergency_contacts.postal_code_a = postal_code_a
        emergency_contacts.postal_town_a = postal_town_a
        emergency_contacts.relationship_a = relationship_a

        emergency_contacts.first_name_b = first_name_b
        emergency_contacts.last_name_b = last_name_b
        emergency_contacts.email_b = email_b
        emergency_contacts.phone_number_b = phone_number_b
        emergency_contacts.postal_box_b = postal_box_b
        emergency_contacts.postal_code_b = postal_code_b
        emergency_contacts.postal_town_b = postal_town_b
        emergency_contacts.relationship_b = relationship_b
        emergency_contacts.save()

        # Save Academic Background
        academic_background.name_of_secondary_school = name_of_secondary_school
        academic_background.index_number_of_secondary_school = index_number_of_secondary_school
        academic_background.year_of_completion_of_secondary_school = year_of_completion_of_secondary_school
        academic_background.name_of_primary_school = name_of_primary_school
        academic_background.index_number_of_primary_school = index_number_of_primary_school
        academic_background.year_of_completion_of_primary_school = year_of_completion_of_primary_school
        academic_background.kcpe_results = kcpe_results
        academic_background.any_other_institution_atttended_and_qualifications_attained = any_other_institution_atttended_and_qualifications_attained
        academic_background.save()


        selected_level = CourseLevel.objects.get(id=level_id)

        if not student.is_registered:
            student.is_registered = True
            student.save()

        if not student.level:
            student.level = selected_level
            student.save()


        messages.success(request, "Profile completed successfully.")
        return redirect('/dashboard/student_dashboard/')

    # For GET or other methods, render the form template (assuming you have one)
    return render(request, 'Dashboard/complete_profile.html', {
        'personal_data': personal_data,
        'family_information': family_information,
        'residence': residence,
        'emergency_contacts': emergency_contacts,
        'academic_background': academic_background,
        'NATIONALITY_CHOICES': NATIONALITY_CHOICES,
        'COUNTY_CHOICES': COUNTY_CHOICES,
        'GENDER_CHOICES': GENDER_CHOICES,
        'Yes_or_No_CHOICES': Yes_or_No_CHOICES,
        'RELIGION_CHOICES': RELIGION_CHOICES,
        'MARITAL_CHOICES': MARITAL_CHOICES,
        'STATUS': STATUS,
        'student_course': student_course,
        'student_course_levels': student_course_levels,


    })
