# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def journal_test(request):
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
    return render(request, 'students/attendance.html', {'students': students})