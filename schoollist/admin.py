from django.contrib import admin
from .models import teachers, students, grade

# Register your models here.
admin.site.register(teachers)
admin.site.register(students)
admin.site.register(grade)