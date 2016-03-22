# -*- coding: utf-8 -*-

from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Student, Group
from django.contrib import messages



# Views for Students
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

    # paginate students
    paginator = Paginator(students, 5)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        students = paginator.page(paginator.num_pages)



    return render(request, 'students/students_list.html',{'students': students,
                                                          'groups': Group.objects.all().order_by('title')})


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
