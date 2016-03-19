from django.contrib import admin
from .models import Student, Group, Professor, LectorLevel, LectorPositions, Exams


# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Professor)
admin.site.register(LectorLevel)
admin.site.register(LectorPositions)
admin.site.register(Exams)
