from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from parkapp.models import Park 

class ParkSerializer(GeoFeatureModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Park
        geo_field = 'location'
        id_field = False 
        fields = ('id','username','park_id','park_name','lat','lng','capacity','empty_capacity','work_hours','park_type','free_time','district','is_open',)
    
    def get_username(self,obj):
        return str(obj.user.username)


class ParkUpdateCreateSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Park
        geo_field = 'location'
        id_field = False 
        fields = ('id','park_id','park_name','lat','lng','capacity','empty_capacity','work_hours','park_type','free_time','district','is_open',)
