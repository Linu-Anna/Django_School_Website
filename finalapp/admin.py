from django.contrib import admin

from .models import Department
admin.site.register(Department)
from .models import Course
admin.site.register(Course)
