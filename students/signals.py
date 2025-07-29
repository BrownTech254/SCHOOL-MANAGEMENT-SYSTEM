from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Student)
def create_student_information(sender, instance, **kwargs):
	Student_Personal_Data.objects.get_or_create(student=instance)
	Student_Family_Information.objects.get_or_create(student=instance)
	Student_Residence.objects.get_or_create(student=instance)
	Student_Emergency_Contact_Persons.objects.get_or_create(student=instance)
	Academic_Background.objects.get_or_create(student=instance)

