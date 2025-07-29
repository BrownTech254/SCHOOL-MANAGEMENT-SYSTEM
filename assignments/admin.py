from django.contrib import admin
from .models import Assignment, AssignmentSubmission
# Register your models here.

admin.site.register(AssignmentSubmission)
admin.site.register(Assignment)