# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Views for Students
def students_list(request):
    students = (
    {'id': 1,
    'first_name': u'Тарас',
    'last_name': u'Гуцалюк',
    'ticket': 235,
    'image': 'img/IMG_1936.JPG'},

    {'id': 2,
    'first_name': u'Рома',
    'last_name': u'Нікітюк',
    'ticket': 666,
    'image': 'img/roma.jpg'},

    {'id': 3,
    'first_name': u'Макс',
    'last_name': u'Кушнір',
    'ticket': 212,
    'image': 'img/maks.jpg'},

    {'id': 4,
    'first_name': u'Райд',
    'last_name': u'Арфуа',
    'ticket': 123,
    'image': 'img/raid.jpg'},

    {'id': 5,
    'first_name': u'Настя',
    'last_name': u'Мошенська',
    'ticket': 562,
    'image': 'img/nastya.jpg'},
    )
    return render(request, 'students/students_list.html', {'students' : students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


# Views for Groups
def groups_list(request):
    groups = (
    {'group_id': 1,
    'group_name': u'Механіка',
    'leader': u'Тарас Гуцалюк'},

    {'group_id': 2,
    'group_name': u'Статистика',
    'leader': u'Райд Арфуа'},

    {'group_id': 3,
    'group_name': u'Математика',
    'leader': u'Мошенська Настя'},
    )
    return render(request, 'students/groups.html', {'groups' : groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
