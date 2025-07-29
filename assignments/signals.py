from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Assignment, AssignmentSubmission
from students.models import Student

@receiver(post_save, sender=Assignment)
def create_student_assignments(sender, instance, **kwargs):
	students = Student.objects.filter(level=instance.unit.level) #student in the same level as the assignment level

	#getting each student in the level of the assignment level
	for student in students:
		AssignmentSubmission.objects.get_or_create(assignment=instance, student=student)
