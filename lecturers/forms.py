from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField as PhoneNumberFormField
from students.counties import *
from students.countries import *


class LecturerPersonalDataForm(forms.ModelForm):
	first_name = forms.CharField(
		label=False,
		required=True,
		)
	last_name = forms.CharField(
		label=False,
		required=True,
		)
	email = forms.EmailField(
		label=False,
		required=True,
		)
	passport_image = forms.ImageField(
		label=False,
		required=True,
		)
	national_id = forms.CharField(
		label=False,
		required=True,
		)
	huduma_number= forms.CharField(
		label=False,
		required=False,
		)
	date_of_birth = forms.DateField(
		label=False,
		required=True,
		)
	gender = forms.ChoiceField(
		label=False,
		choices=GENDER_CHOICES,
		widget=forms.Select(attrs={'class': 'form-control'}),
		required=True,
		)
	marital_status = forms.ChoiceField(
		label=False,
		choices=MARITAL_CHOICES,
		widget=forms.Select(attrs={'class': 'form-control'}),
		required=True,

		)
	name_of_spouse_if_married = forms.CharField(
		label=False,
		required=False,

		)
	number_of_children_if_married = forms.CharField(
		label=False,
		required=False,
		)
	occupation_of_spouse_if_married = forms.CharField(
		label=False,
		required=False,
		)
	phone_number_of_spouse_if_married = PhoneNumberFormField(
		label=False,
		required=False,
		)
	physical_impairement = forms.ChoiceField(
		label=False,
		choices=Yes_or_No_CHOICES,
		widget=forms.Select(attrs={'class': 'form-control'}),
		required=True,


		)
	if_physical_impairment = forms.CharField(
		label=False,
		widget=forms.Textarea(attrs={'row': 4, 'placeholder': 'describe your impairement if any'}),
		required=False,
		)
	nhif_number = forms.CharField(
		label=False,
		required=False,
		)
	religion = forms.ChoiceField(
		label=False,
		choices=RELIGION_CHOICES,
		widget=forms.Select(attrs={'class': 'form-control'}),
		required=True,
		)
	nationality = forms.ChoiceField(
		label=False,
		choices=NATIONALITY_CHOICES,
		widget=forms.Select(attrs={'class': 'form-control'}),
		required=True,
		)
	phone_number = PhoneNumberFormField(
		label=False,
		required=True,
		)
	postal_box = forms.IntegerField(
		label=False,
		required=True,
		)
	postal_code = forms.CharField(
		label=False,
		required=True,
		)
	postal_town = forms.CharField(
		label=False,
		required=True,
		)


	class Meta:
		model = Lecturer_Personal_Data
		#fields = '__all__'
		exclude = ['lecturer']

	def __init__(self, *args, **kwargs):
		super().__init__( *args, **kwargs)

		self.fields['marital_status'].required = True
		self.fields['physical_impairement'].required = True

	def clean(self):
		cleaned_data = super().clean()

		#extract value , during submittion our data passes through the code
		marital_status = cleaned_data.get("marital_status")
		physical_impairement = cleaned_data.get("physical_impairement")
		name_of_spouse_if_married = cleaned_data.get("name_of_spouse_if_married")
		occupation_of_spouse_if_married = cleaned_data.get("occupation_of_spouse_if_married")
		number_of_children_if_married = cleaned_data.get("number_of_children_if_married")
		phone_number_of_spouse_if_married = cleaned_data.get("phone_number_of_spouse_if_married")
		if_physical_impairment = cleaned_data.get("if_physical_impairment")

		if marital_status == "Married":
			if not name_of_spouse_if_married:
				self.add_error('name_of_spouse_if_married', 'please provide the name of your spouse')
			if not occupation_of_spouse_if_married:
				self.add_error('occupation_of_spouse_if_married', 'please provide the spouse"s occupation')
			if not number_of_children_if_married:
				self.add_error('number_of_children_if_married', 'please provide the number of children ')
			if not phone_number_of_spouse_if_married:
				self.add_error('phone_number_of_spouse_if_married', 'please provide the phone number of spouse ')

		if physical_impairement == "Yes":
			if not if_physical_impairment:
				self.add_error('if_physical_impairment', 'please describe  the impairement')
			
		return cleaned_data



class LecturerFamilyInformationForm(forms.ModelForm):
	father_first_name = forms.CharField(label=False, required=True,)
	father_last_name = forms.CharField(label=False, required=True,)
	father_status = forms.ChoiceField(
		label=False,
		choices=STATUS, 
		widget=forms.Select(attrs={'class':'form-control'}),
		required=True,
		)
	father_occupation = forms.CharField(label=False, required=True,)
	father_date_of_birth = forms.DateField(label=False, required=True,)
	mother_first_name = forms.CharField(label=False, required=True,)
	mother_last_name = forms.CharField(label=False, required=True,)
	mother_status = forms.ChoiceField(
		label=False,
		choices=STATUS,
		widget=forms.Select(attrs={'class':'form-control'}),
		required=True,
		)
	mother_occupation = forms.CharField(label=False, required=True,)
	mother_date_of_birth = forms.DateField(label=False, required=True,)
	number_of_brothers_and_sisters = forms.IntegerField(label=False, required=True,)


	class Meta:
		model = Lecturer_Family_Information
		#fields = '__all__'
		exclude = ['lecturer']

class LecturerResidenceForm(forms.ModelForm):
	place_of_birth = forms.CharField(label=False, required=True,)
	place_of_permanent_residence = forms.CharField(label=False, required=True,)
	nearest_town = forms.CharField(label=False, required=True,)
	location = forms.CharField(label=False, required=True,)
	name_of_chief = forms.CharField(label=False, required=True,)
	county = forms.ChoiceField(
		label=False,
		choices=COUNTY_CHOICES,
		widget=forms.Select(attrs={'class':'form-control'}),
		required=True,
		)
	sub_county = forms.CharField(label=False, required=True,)
	constituency = forms.CharField(label=False, required=True,)
	nearest_police_station = forms.CharField(label=False, required=True,)

	class Meta:
		model = Lecturer_Residence
		#fields = '__all__'
		exclude = ['lecturer']


class LecturerEmergencyContactPersonsForm(forms.ModelForm):
	first_name_a = forms.CharField(label=False, required=True, )
	last_name_a = forms.CharField(label=False, required=True, )
	email_a = forms.EmailField(label=False, required=True, )
	phone_number_a = PhoneNumberFormField(label=False, required=True,)
	postal_box_a = forms.IntegerField(label=False, required=True,)
	postal_code_a = forms.CharField(label=False, required=True, )
	postal_town_a = forms.CharField(label=False, required=True, )
	relationship_a = forms.CharField(label=False, required=True, )
	first_name_b = forms.CharField(label=False, required=True, )
	last_name_b = forms.CharField(label=False, required=True, )
	email_b = forms.EmailField(label=False, required=True, )
	phone_number_b = PhoneNumberFormField(label=False, required=True,)
	postal_box_b = forms.IntegerField(label=False, required=True, )
	postal_code_b = forms.CharField(label=False, required=True, )
	postal_town_b = forms.CharField(label=False, required=True, )
	relationship_b = forms.CharField(label=False, required=True, )
	class Meta:
		model = Lecturer_Emergency_Contact_Persons
		#fields = '__all__'
		exclude = ['lecturer']


class AcademicBackgroundForm(forms.ModelForm):
	name_of_secondary_school = forms.CharField(label=False, required=True,)
	index_number_of_secondary_school = forms.IntegerField(label=False, required=True,)
	year_of_completion_of_secondary_school = forms.IntegerField(label=False, required=True,)
	name_of_primary_school = forms.CharField(label=False, required=True,)
	index_number_of_primary_school = forms.IntegerField(label=False, required=True,)
	year_of_completion_of_primary_school = forms.IntegerField(label=False, required=True,)
	kcpe_results = forms.CharField(
		label=False,
		widget=forms.Textarea(attrs={'row':3}),
		required=True,
		)
	any_other_institution_atttended_and_qualifications_attained = forms.CharField(
		label=False,
		widget=forms.Textarea(attrs={'row':4}),
		required=True,
		)

	class Meta:
		model = Academic_Background
		#fields = ['lecturer', 'name_of_secondary_school', 'index_number_of_secondary_school', 'year_of_completion_of_secondary_school', 'name_of_primary_school']
		exclude = ['lecturer']
	
