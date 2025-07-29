from django.contrib import messages
from django.shortcuts import redirect

if not first_name or first_name == "None":
	messages.warning(request, "You should provide your first name")
	return redirect('/dashboard/')

if not last_name or last_name == "None":
	messages.warning(request, "You should provide your last name")
	return redirect('/dashboard/')

if not email or email == "None":
	messages.warning(request, "You should provide an email address")
	return redirect('/dashboard/')

if not passport_image:
	messages.warning(request, "You should upload a passport image")
	return redirect('/dashboard/')

if not national_id or national_id == "None":
	messages.warning(request, "You should provide your national ID")
	return redirect('/dashboard/')

if not huduma_number or huduma_number == "None":
	messages.warning(request, "You should provide your Huduma number")
	return redirect('/dashboard/')

if not date_of_birth or date_of_birth == "None":
	messages.warning(request, "You should provide your date of birth")
	return redirect('/dashboard/')

if not gender or gender == "None":
	messages.warning(request, "You should select your gender")
	return redirect('/dashboard/')

if not marital_status or marital_status == "None":
	messages.warning(request, "You should select your marital status")
	return redirect('/dashboard/')

if not name_of_spouse_if_married or name_of_spouse_if_married == "None":
	messages.warning(request, "You should provide your spouse's name")
	return redirect('/dashboard/')

if not number_of_children_if_married or number_of_children_if_married == "None":
	messages.warning(request, "You should provide number of children")
	return redirect('/dashboard/')

if not occupation_of_spouse_if_married or occupation_of_spouse_if_married == "None":
	messages.warning(request, "You should provide your spouse's occupation")
	return redirect('/dashboard/')

if not phone_number_of_spouse_if_married or phone_number_of_spouse_if_married == "None":
	messages.warning(request, "You should provide your spouse's phone number")
	return redirect('/dashboard/')

if not physical_impairement or physical_impairement == "None":
	messages.warning(request, "You should indicate physical impairment")
	return redirect('/dashboard/')

if not if_physical_impairment or if_physical_impairment == "None":
	messages.warning(request, "You should describe your physical impairment")
	return redirect('/dashboard/')

if not nhif_number or nhif_number == "None":
	messages.warning(request, "You should provide your NHIF number")
	return redirect('/dashboard/')

if not religion or religion == "None":
	messages.warning(request, "You should select your religion")
	return redirect('/dashboard/')

if not nationality or nationality == "None":
	messages.warning(request, "You should select your nationality")
	return redirect('/dashboard/')

if not phone_number or phone_number == "None":
	messages.warning(request, "You should provide your phone number")
	return redirect('/dashboard/')

if not postal_box or postal_box == "None":
	messages.warning(request, "You should provide your postal box")
	return redirect('/dashboard/')

if not postal_code or postal_code == "None":
	messages.warning(request, "You should provide your postal code")
	return redirect('/dashboard/')

if not postal_town or postal_town == "None":
	messages.warning(request, "You should provide your postal town")
	return redirect('/dashboard/')

if not father_first_name or father_first_name == "None":
    messages.warning(request, "You should provide your father's first name")
    return redirect('/dashboard/')

if not father_last_name or father_last_name == "None":
    messages.warning(request, "You should provide your father's last name")
    return redirect('/dashboard/')

if not father_status or father_status == "None":
    messages.warning(request, "You should indicate your father's status")
    return redirect('/dashboard/')

if not father_occupation or father_occupation == "None":
    messages.warning(request, "You should provide your father's occupation")
    return redirect('/dashboard/')

if not father_date_of_birth or father_date_of_birth == "None":
    messages.warning(request, "You should provide your father's date of birth")
    return redirect('/dashboard/')

if not mother_first_name or mother_first_name == "None":
    messages.warning(request, "You should provide your mother's first name")
    return redirect('/dashboard/')

if not mother_last_name or mother_last_name == "None":
    messages.warning(request, "You should provide your mother's last name")
    return redirect('/dashboard/')

if not mother_status or mother_status == "None":
    messages.warning(request, "You should indicate your mother's status")
    return redirect('/dashboard/')

if not mother_occupation or mother_occupation == "None":
    messages.warning(request, "You should provide your mother's occupation")
    return redirect('/dashboard/')

if not mother_date_of_birth or mother_date_of_birth == "None":
    messages.warning(request, "You should provide your mother's date of birth")
    return redirect('/dashboard/')

if not number_of_brothers_and_sisters or number_of_brothers_and_sisters == "None":
    messages.warning(request, "You should provide the number of brothers and sisters")
    return redirect('/dashboard/')

# Contact Person A
if not first_name_a or first_name_a == "None":
    messages.warning(request, "You should provide the first name of emergency contact person A")
    return redirect('/dashboard/')

if not last_name_a or last_name_a == "None":
    messages.warning(request, "You should provide the last name of emergency contact person A")
    return redirect('/dashboard/')

if not email_a or email_a == "None":
    messages.warning(request, "You should provide the email of emergency contact person A")
    return redirect('/dashboard/')

if not phone_number_a or phone_number_a == "None":
    messages.warning(request, "You should provide the phone number of emergency contact person A")
    return redirect('/dashboard/')

if not postal_box_a or postal_box_a == "None":
    messages.warning(request, "You should provide the postal box of emergency contact person A")
    return redirect('/dashboard/')

if not postal_code_a or postal_code_a == "None":
    messages.warning(request, "You should provide the postal code of emergency contact person A")
    return redirect('/dashboard/')

if not postal_town_a or postal_town_a == "None":
    messages.warning(request, "You should provide the postal town of emergency contact person A")
    return redirect('/dashboard/')

if not relationship_a or relationship_a == "None":
    messages.warning(request, "You should provide the relationship of emergency contact person A")
    return redirect('/dashboard/')


# Contact Person B
if not first_name_b or first_name_b == "None":
    messages.warning(request, "You should provide the first name of emergency contact person B")
    return redirect('/dashboard/')

if not last_name_b or last_name_b == "None":
    messages.warning(request, "You should provide the last name of emergency contact person B")
    return redirect('/dashboard/')

if not email_b or email_b == "None":
    messages.warning(request, "You should provide the email of emergency contact person B")
    return redirect('/dashboard/')

if not phone_number_b or phone_number_b == "None":
    messages.warning(request, "You should provide the phone number of emergency contact person B")
    return redirect('/dashboard/')

if not postal_box_b or postal_box_b == "None":
    messages.warning(request, "You should provide the postal box of emergency contact person B")
    return redirect('/dashboard/')

if not postal_code_b or postal_code_b == "None":
    messages.warning(request, "You should provide the postal code of emergency contact person B")
    return redirect('/dashboard/')

if not postal_town_b or postal_town_b == "None":
    messages.warning(request, "You should provide the postal town of emergency contact person B")
    return redirect('/dashboard/')

if not relationship_b or relationship_b == "None":
    messages.warning(request, "You should provide the relationship of emergency contact person B")
    return redirect('/dashboard/')

# Academic Background
if not name_of_secondary_school or name_of_secondary_school == "None":
    messages.warning(request, "You should provide the name of your secondary school")
    return redirect('/dashboard/')

if not index_number_of_secondary_school or index_number_of_secondary_school == "None":
    messages.warning(request, "You should provide your secondary school index number")
    return redirect('/dashboard/')

if not year_of_completion_of_secondary_school or year_of_completion_of_secondary_school == "None":
    messages.warning(request, "You should provide the year you completed secondary school")
    return redirect('/dashboard/')

if not name_of_primary_school or name_of_primary_school == "None":
    messages.warning(request, "You should provide the name of your primary school")
    return redirect('/dashboard/')

if not index_number_of_primary_school or index_number_of_primary_school == "None":
    messages.warning(request, "You should provide your primary school index number")
    return redirect('/dashboard/')

if not year_of_completion_of_primary_school or year_of_completion_of_primary_school == "None":
    messages.warning(request, "You should provide the year you completed primary school")
    return redirect('/dashboard/')

if not kcpe_results or kcpe_results == "None":
    messages.warning(request, "You should provide your KCPE results")
    return redirect('/dashboard/')

if not any_other_institution_atttended_and_qualifications_attained or any_other_institution_atttended_and_qualifications_attained == "None":
    messages.warning(request, "You should provide any other institutions attended and qualifications attained")
    return redirect('/dashboard/')