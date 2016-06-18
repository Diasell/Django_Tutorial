from rest_framework import serializers

from .models.schedule import Para, ParaTime, WorkingDay
from .models.disciplines import Disciplines
from .models.rooms import Rooms
from .models.professor import Professor
from .models.groups import Group


class DisciplinesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplines
        fields = (
            'discipline',
        )


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rooms
        fields = (
            'room',
        )


class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'position',
            'photo',
        )


class ParaTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParaTime
        fields = (
            'para_starttime',
            'para_endtime',
            'para_position',
        )


class WorkingDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkingDay
        fields = (
            'dayoftheweek',
        )


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            'title',
            'leader',
        )


class ParaSerializer(serializers.ModelSerializer):

    para_subject = DisciplinesSerializer(read_only=True)
    para_room = RoomSerializer(read_only=True)
    para_professor = ProfessorSerializer(read_only=True)
    para_number = ParaTimeSerializer(read_only=True)
    para_day = WorkingDaySerializer(read_only=True)
    para_group = GroupSerializer(read_only=True)

    class Meta:
        model = Para
        fields = (
            'para_subject',
            'para_room',
            'para_professor',
            'para_number',
            'para_day',
            'para_group',
            'week_type',
        )
