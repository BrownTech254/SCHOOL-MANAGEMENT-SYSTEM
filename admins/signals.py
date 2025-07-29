from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Lecturer)
def create_admin_information(sender, instance, **kwargs):
	Admin_Personal_Data.objects.get_or_create(admin=instance)
	Admin_Family_Information.objects.get_or_create(admin=instance)
	Admin_Residence.objects.get_or_create(admin=instance)
	Admin_Emergency_Contact_Persons.objects.get_or_create(admin=instance)
	Academic_Background.objects.get_or_create(admin=instance)
