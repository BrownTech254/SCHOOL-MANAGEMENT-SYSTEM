from django.contrib import admin
from . models import Department, Course, CourseLevel, LevelUnit

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(CourseLevel)
admin.site.register(LevelUnit)