from django.db import models
from students.countries import NATIONALITY_CHOICES
from students.counties import COUNTY_CHOICES
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import CustomeUser


# Create your models here.
GENDER_CHOICES = [
	('Male','Male'),
	('Female','Female'),
	('Rather Not Say','Rather Not Say'),
]

Yes_or_No_CHOICES = [
	('Yes','Yes'),
	('No','No'),	
]

RELIGION_CHOICES = [
	('Christian','Christian'),
	('Muslim', 'Muslim'),
	('Hindu', 'Hindu'),
	('Pagan', 'Pagan')
]

MARITAL_CHOICES = [
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
    ('Other', 'Other'),
    ('Prefer not to say', 'Prefer not to say'),
]

STATUS = [
    ('Alive', 'Alive'),
    ('Deceased', 'Deceased'),
    ('Unknown', 'Unknown'),
]

class Lecturer(models.Model):
	user = models.OneToOneField(CustomeUser, on_delete=models.CASCADE, related_name='lecturer')
	first_name = models.CharField(max_length=255, null=True,blank=True)
	last_name = models.CharField(max_length=255, null=True,blank=True)
	registration_number = models.CharField(max_length=255, null=True,blank=True)
	is_registered = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username


class Lecturer_Personal_Data(models.Model):
	lecturer = models.OneToOneField(Lecturer, on_delete=models.CASCADE, related_name='personal_data')
	first_name = models.CharField(max_length=255, null=True,blank=True)
	last_name = models.CharField(max_length=255, null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
	passport_image = models.ImageField(upload_to='student_photos', null=True,blank=True)
	national_id = models.CharField(max_length=255, null=True,blank=True)
	huduma_number = models.CharField(max_length=255, null=True,blank=True)
	date_of_birth = models.DateField(max_length=255, null=True,blank=True)
	gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default="Rather Not Say")
	marital_status = models.CharField(max_length=255, choices=MARITAL_CHOICES, default="Single")
	name_of_spouse_if_married = models.CharField(max_length=255,null=True,blank=True)
	number_of_children_if_married = models.CharField(null=True,blank=True)
	occupation_of_spouse_if_married = models.CharField(max_length=255,null=True,blank=True)
	phone_number_of_spouse_if_married = PhoneNumberField(null=True,blank=True)
	physical_impairement = models.CharField(max_length=255, choices=Yes_or_No_CHOICES, default="No")
	if_physical_impairment = models.TextField(null=True, blank=True)
	nhif_number = models.CharField(max_length=255, null=True, blank=True)
	religion = models.CharField(max_length=255, choices=RELIGION_CHOICES, default="Pagan")
	nationality = models.CharField(max_length=255, choices=NATIONALITY_CHOICES, default="Kenyan")
	phone_number = PhoneNumberField(null=True,blank=True)
	postal_box = models.CharField(null=True,blank=True)
	postal_code = models.CharField(max_length=255, null=True,blank=True)
	postal_town = models.CharField(max_length=255, null=True,blank=True)


	def __str__(self):
		return self.lecturer.user.username

	def save(self, *args, **kwargs):
		if self.first_name is None:
			self.first_name = self.lecturer.user.first_name
		if self.last_name is None:
			self.last_name = self.lecturer.user.last_name
		if self.email is None:
			self.email = self.lecturer.user.email

		super().save(*args, **kwargs)

class Lecturer_Family_Information(models.Model):
	lecturer = models.OneToOneField(Lecturer, on_delete=models.CASCADE, related_name='family')
	father_first_name = models.CharField(max_length=255, null=True,blank=True)
	father_last_name = models.CharField(max_length=255, null=True,blank=True)
	father_status = models.CharField(max_length=255, choices=STATUS, default="Alive")
	father_occupation = models.CharField(max_length=255, null=True,blank=True)
	father_date_of_birth = models.DateField(null=True,blank=True)
	mother_first_name = models.CharField(max_length=255, null=True,blank=True)
	mother_last_name = models.CharField(max_length=255, null=True,blank=True)
	mother_status = models.CharField(max_length=255, choices=STATUS, default="Alive")
	mother_occupation = models.CharField(max_length=255, null=True,blank=True)
	mother_date_of_birth = models.DateField(null=True,blank=True)
	number_of_brothers_and_sisters = models.CharField(null=True,blank=True)

	def __str__(self):
		return self.lecturer.user.username

class Lecturer_Residence(models.Model):
	lecturer = models.OneToOneField(Lecturer, on_delete=models.CASCADE, related_name='residence')
	place_of_birth = models.CharField(max_length=255, null=True, blank=True)
	place_of_permanent_residence = models.CharField(max_length=255, null=True, blank=True)
	nearest_town = models.CharField(max_length=255, null=True, blank=True)
	location = models.CharField(max_length=255, null=True, blank=True)
	name_of_chief = models.CharField(max_length=255, null=True, blank=True)
	county = models.CharField(max_length=255, choices=COUNTY_CHOICES, default="Nairobi")
	sub_county = models.CharField(max_length=255, null=True, blank=True)
	constituency = models.CharField(max_length=255, null=True, blank=True)
	nearest_police_station = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.lecturer.user.username



class Lecturer_Emergency_Contact_Persons(models.Model):
	lecturer = models.OneToOneField(Lecturer, on_delete=models.CASCADE, related_name='emergency_contacts')
	first_name_a = models.CharField(max_length=255, null=True, blank=True)
	last_name_a = models.CharField(max_length=255, null=True, blank=True)
	email_a = models.EmailField(null=True, blank=True)
	phone_number_a = PhoneNumberField(null=True, blank=True)
	postal_box_a = models.CharField(null=True, blank=True)
	postal_code_a = models.CharField(max_length=255, null=True, blank=True)
	postal_town_a = models.CharField(max_length=255, null=True, blank=True)
	relationship_a = models.CharField(max_length=255, null=True, blank=True)
	first_name_b = models.CharField(max_length=255, null=True, blank=True)
	last_name_b = models.CharField(max_length=255, null=True, blank=True)
	email_b = models.EmailField(null=True, blank=True)
	phone_number_b = PhoneNumberField(null=True, blank=True)
	postal_box_b = models.CharField(null=True, blank=True)
	postal_code_b = models.CharField(max_length=255, null=True, blank=True)
	postal_town_b = models.CharField(max_length=255, null=True, blank=True)
	relationship_b = models.CharField(max_length=255, null=True, blank=True)


	def __str__(self):
		return self.lecturer.user.username


class Academic_Background(models.Model):
	lecturer = models.OneToOneField(Lecturer, on_delete=models.CASCADE, related_name='academic_data')
	name_of_secondary_school = models.CharField(max_length=255, null=True, blank=True)
	index_number_of_secondary_school = models.CharField(null=True, blank=True)
	year_of_completion_of_secondary_school = models.IntegerField(null=True, blank=True)
	name_of_primary_school = models.CharField(max_length=255, null=True, blank=True)
	index_number_of_primary_school = models.CharField(null=True, blank=True)
	year_of_completion_of_primary_school = models.CharField(null=True, blank=True)
	kcpe_results = models.TextField(null=True, blank=True)
	any_other_institution_atttended_and_qualifications_attained = models.TextField(null=True,blank=True)

	def __str__(self):
		return self.lecturer.user.username



