# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Student, Group

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
    paginator = Paginator(students, 3)
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

            # TODO validate input from user
            errors = {}

            if not errors:
                # Create student object
                new_student = Student(
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name'],
                    middle_name = request.POST['middle_name'],
                    birthday = request.POST['birthday'],
                    ticket = request.POST['ticket'],
                    student_group = Group.objects.get(pk=request.POST['student_group']),
                    photo = request.FILES['photo'],
                )
                #Saving student to data base
                new_student.save()

                #redirect user to students list page
                return HttpResponseRedirect(reverse('home'))

            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html', {'errors':errors})

        elif request.POST.get('cancel_button') is not None:
            # Redirect user to home page on cancel button
            return HttpResponseRedirect(reverse('home'))

    else:
        # initial form render
        return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})


    return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
