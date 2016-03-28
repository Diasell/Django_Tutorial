from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django.core.urlresolvers import reverse
from .models import Student, Group, Professor, LectorLevel, LectorPositions, Exams

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']

    def get_view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk':obj.id})


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader']
    list_display_links = ['title']
    list_editable = ['leader']
    list_per_page = 5
    search_fields = ['title']

    def get_view_on_site(self, obj=None):
        return reverse('groups_edit', kwargs={'pk':obj.id})


class ExamsAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'5'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})}
    }

    list_display = ['exam_title', 'exam_executor','exam_group', 'room', 'date_time']
    list_filter = ['exam_title', 'exam_executor', 'exam_group', 'date_time']
    list_display_links = ['exam_title', 'exam_executor', 'exam_group']
    list_editable = ['room']
    list_per_page = 5
    search_fields = ['exam_title', 'room']

    def get_view_on_site(self, obj=None):
        return reverse('exams', kwargs={'pk':obj.id})


class ProfessorAdmin(admin.ModelAdmin):

    list_display = ['photo', 'last_name', 'first_name', 'middle_name', 'level', 'position']
    list_filter = ['level', 'position']
    list_display_links = ['last_name', 'first_name', 'middle_name']
    list_per_page = 10
    search_fields = ['last_name', 'first_name']

    def get_view_on_site(self, obj=None):
        return reverse('exams', kwargs={'pk':obj.id})

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(LectorLevel)
admin.site.register(LectorPositions)
admin.site.register(Exams, ExamsAdmin)
