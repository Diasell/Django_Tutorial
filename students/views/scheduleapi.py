from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializer import ParaSerializer
from ..models.schedule import Para

class ParaListApiView(APIView):

    def get(self, request, format=None):
        paru = Para.objects.all()
        serializer = ParaSerializer(paru, many=True)
        return  Response(serializer.data)