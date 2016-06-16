from tastypie.resources import ModelResource
from .models.schedule import Para

class ParaResource(ModelResource):

    class Meta:
        queryset = Para.objects.all()
        resource_name = "paru"