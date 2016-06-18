from django.conf.urls import url
from .views.scheduleapi import ParaListApiView

urlpatterns = [
    url(r'^$', ParaListApiView.as_view(), name='para_list'),

]
