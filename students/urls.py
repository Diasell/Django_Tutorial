from django.conf.urls import url
from .views.api import *

urlpatterns = [
    url(r'^$', ParaListApiView.as_view(), name='para_list'),
    url(r'(?P<pk>\d+)/$',
        RetrieveUpdateDestroyPara.as_view(),
        name='para_detail'),
    url(r'^(?P<para_pk>\d+)/discipline/$',
        ListCreateDisciplines.as_view(),
        name='discipline'
        ),
    url(r'^(?P<para_pk>\d+)/room/$',
        ListCreateRooms.as_view(),
        name='room'
        ),

]
