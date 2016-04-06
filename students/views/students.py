# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..util import paginate

from django.views.generic.base import TemplateView

from ..models.students import Student
from ..models.groups import Group

from django.contrib import messages
from django.views.generic import UpdateView, DeleteView

from django.forms import ModelForm, ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from ..util import paginate, get_current_group



class StudentsListView(TemplateView):
    template_name = 'students/students_list.html'

    def get_context_data(self, **kwargs):

        context = super(StudentsListView, self).get_context_data(**kwargs)

        # check if we need to show only 1 group of students:
        current_group = get_current_group(self.request)
        if current_group:
            students = Student.objects.filter(student_group=current_group)
        else:
            # otherwise show all students
            students = Student.objects.all()
        # ordering students by last_name when 1st time on the page:
        if self.request.path == '/':
            students = students.order_by('last_name')

        # try to order students list
        order_by = self.request.GET.get('order_by', '')
        if order_by in ('last_name', 'first_name', 'ticket'):
            students = students.order_by(order_by)
            if self.request.GET.get('reverse', '') == '1':
                students = students.reverse()

        context['students'] = students
        context['groups'] = Group.objects.all().order_by('title')

        # paginate students
        context = paginate(students, 10, self.request, context, var_name='students')

        return context

"""# Views for Students
def students_list(request):
    students = Student.objects.all()
    # ordering students by last_name when 1st time on the page:
    if request.path == '/':
        students = students.order_by('last_name')

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    context['students'] = students
    context['groups'] = Group.objects.all().order_by('title')
    # paginate students
    context = paginate(students, 5, request, context)

    print context

    return render(request, 'students/students_list.html', context)"""


def students_add(request):
    # was form posted?
    if request.method == "POST":

        # was form add button clicked?
        if request.POST.get("add_button") is not None:

            # errors collection
            errors = {}

            # validated students data will fo here
            data = {'middle_name':request.POST.get('middle_name'),
                    'notes':request.POST.get('notes')}

            # validate user input

            first_name = request.POST.get('first_name','').strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name','').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday','').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                if photo.size>(2048*1024):
                    errors['photo'] = u"Розмір фотографії не повинен перевищувати 2 МБ"
                elif not('image' in photo.content_type):
                    errors['photo'] = u"Тип вибраного вами файлу не є зображенням"
                else:
                    data['photo'] = photo


            # save student
            if not errors:
                student = Student(**data)
                student.save()
                # redirect to students list page
                message_st_added = u'Cтудент %s %s успішно доданий!' % (student.last_name, student.first_name)
                messages.success(request, message_st_added)
                return HttpResponseRedirect(reverse('home'))
            else:
                # render form with errors and previous user input
                message_wrong_input = u'Будь-ласка, виправте наступні помилки'
                messages.warning(request, message_wrong_input)
                return render(request, 'students/students_add.html',{'groups': Group.objects.all().order_by('title'),
                                                                     'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # Redirect user to home page on cancel button
            message_cancel_clicked = u'Додавання студента скасовано!'
            messages.info(request, message_cancel_clicked)
            return HttpResponseRedirect(reverse('home'))

    else:
        # initial form render
        return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})


    return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


class StudentUpdateForm(ModelForm):

    class Meta:
        model = Student
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args,**kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('students_edit', kwargs={'pk':kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        #set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        #add buttons
        self.helper.layout[-1]=FormActions(
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link")
        )


    def clean_student_group(self):
        """
        Checks if student is not a leader in any other group.
        If yes, we need to ensure that it is the same group as selected
        """
        # get groups where current student is a leader:
        groups = Group.objects.filter(leader = self.instance)

        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(u"Студент є старостою іншої групи.", code='invalid')
        else:
            return self.cleaned_data['student_group']


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):

        return u'%s?status_message=студента успішно збережено!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            cancel_message = u'Редагування студента відмінено!'
            messages.info(request, cancel_message)
            return HttpResponseRedirect(u'%s?status_message=Редагування студента відмінено!' % reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'

    def get_success_url(self):
        return u'%s?Status_message=Студента успішно видалено!' % reverse('home')
