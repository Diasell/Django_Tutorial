# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from django.db import models
from django.forms import TextInput, Textarea, ModelForm, ValidationError
from django.core.urlresolvers import reverse

from .models import Student, Group, Professor, LectorLevel, LectorPositions, MonthJournal, Exams, Disciplines
from .models.rooms import Rooms
from .models.schedule import *

from django.utils.translation import ugettext as _

class StudentFormAdmin(ModelForm):

    def clean_student_group(self):
        """
        Checks if student is not a leader in any other group.
        If yes, we need to ensure that it is the same group as selected
        """
        # get groups where current student is a leader:
        groups = Group.objects.filter(leader = self.instance)

        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(_(u"Student is a member of another group"), code='invalid')
        else:
            return self.cleaned_data['student_group']


class GroupFormAdmin(ModelForm):

    def clean_leader(self):
        """
        Check if selected student belongs to the group. If not then he cant be a leader
        of this group
        """
        # gets all students that belongs to selected group
        group_students = Student.objects.filter(student_group = self.instance)

        if len(group_students)>0 and self.cleaned_data['leader'] not in group_students:
            raise ValidationError(_(u"Student do not belong to the current group"), code='invalid')
        else:
            return self.cleaned_data['leader']

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['last_name', 'first_name', 'ticket', 'student_group']
#     list_display_links = ['last_name', 'first_name']
#     list_filter = ['student_group']
#     list_per_page = 10
#     search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']
#
#     form = StudentFormAdmin
#
#     actions = ['duplicate_sel_student']
#
#     def get_view_on_site(self, obj):
#         return reverse('students_edit', kwargs={'pk':obj.id})
#
#     def duplicate_sel_student(self, request, queryset):
#         for object in queryset:
#             object.id = None
#             object.save()
#
#         rows_updated = queryset.count()
#         if rows_updated == 1:
#             user_message = _(u"1 student was successfully dupicated")
#         else:
#             user_message = -_(u"%(rows_updated)s students were successfully dupicated") % {'rows_updated':rows_updated}
#         self.message_user(request, user_message)
#     duplicate_sel_student.short_description = "Duplicate"


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader']
    list_display_links = ['title']
    list_editable = ['leader']
    list_per_page = 5
    search_fields = ['title']

    form = GroupFormAdmin

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



class ParaAdmin(admin.ModelAdmin):

    list_display = ['para_number', 'para_day', 'para_subject', 'para_group', 'para_room', 'para_professor']
    list_display_links = ['para_subject', 'para_group']
    list_filter = ['para_subject', 'para_group', 'para_room', 'para_professor', 'para_number', 'para_day']
    list_per_page = 100
    search_fields = ['para_subject', 'para_group', 'para_room', 'para_professor', 'para_number', 'para_day']



class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Student'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Register your models here.
#admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(LectorLevel)
admin.site.register(LectorPositions)
admin.site.register(Exams, ExamsAdmin)
admin.site.register(MonthJournal)
admin.site.register(Rooms)
admin.site.register(Disciplines)
admin.site.register(Para, ParaAdmin)
admin.site.register(WorkingDay)
admin.site.register(ParaTime)
admin.site.register(StartSemester)


