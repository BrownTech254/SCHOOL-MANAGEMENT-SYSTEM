from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Lecturer)
def create_lecturer_information(sender, instance, **kwargs):
	Lecturer_Personal_Data.objects.get_or_create(lecturer=instance)
	Lecturer_Family_Information.objects.get_or_create(lecturer=instance)
	Lecturer_Residence.objects.get_or_create(lecturer=instance)
	Lecturer_Emergency_Contact_Persons.objects.get_or_create(lecturer=instance)
	Academic_Background.objects.get_or_create(lecturer=instance)
