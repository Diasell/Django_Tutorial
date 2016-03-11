# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

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
