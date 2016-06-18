from rest_framework import serializers
from .models.schedule import Para, ParaTime
from .models.disciplines import Disciplines


class DisciplinesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplines
        fields = (
            'discipline'
        )

class ParaTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParaTime
        fields = (
            'para_starttime',
            'para_endtime',
            'para_position'
        )


class ParaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Para
        fields = (
            'para_subject',
            'para_room',
            'para_professor',
            'para_number',
            'para_day',
            'para_group',
            'week_type'
        )