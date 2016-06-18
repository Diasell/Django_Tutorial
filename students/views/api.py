from rest_framework import generics
from rest_framework import status

from ..serializer import *

from ..models.schedule import Para, ParaTime, WorkingDay
from ..models.disciplines import Disciplines
from ..models.rooms import Rooms
from ..models.professor import Professor
from ..models.groups import Group


class ParaListApiView(generics.ListCreateAPIView):
    queryset = Para.objects.all()
    serializer_class = ParaSerializer


class RetrieveUpdateDestroyPara(generics.RetrieveUpdateDestroyAPIView):
    queryset = Para.objects.all()
    serializer_class = ParaSerializer


class ListCreateDisciplines(generics.ListCreateAPIView):
    queryset = Disciplines.objects.all()
    serializer_class = DisciplinesSerializer

    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs.get('para_pk'))


class ListCreateRooms(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs.get('para_pk'))
