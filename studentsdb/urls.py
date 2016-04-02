"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.views.students import StudentUpdateView, StudentDeleteView, StudentsListView
from students.views.groups import DeleteGroupView, GroupUpdateView, GroupListView
from students.views.exams import ExamsUpdateView
from students.views.journal import JournalView


urlpatterns = [
    # students url
    url(r'^$', StudentsListView.as_view(), name='home'),

    url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),

    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),

    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),


    # Groups urls
    url(r'^groups/$', GroupListView.as_view(), name='groups'),

    url(r'^groups/add/$', 'students.views.groups.groups_add', name='groups_add'),

    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='groups_edit'),

    url(r'^groups/(?P<pk>\d+)/delete/$', DeleteGroupView.as_view(), name='groups_delete'),


    # Exams urls:
    url(r'^exams/$', 'students.views.exams.exams_list', name='exams'),
    url(r'^exams/(?P<pk>\d+)/edit/$', ExamsUpdateView.as_view(), name='exams_edit'),


    # Journal urls:
    url(r'^journal/$', JournalView.as_view(),  name='journal'),

    # Contact-admin
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin'),

    # admin part
    url(r'^admin/', include(admin.site.urls)),
]

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': MEDIA_ROOT}))