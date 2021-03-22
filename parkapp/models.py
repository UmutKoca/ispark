from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Park(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    park_id = models.IntegerField(null=True)
    park_name = models.CharField(max_length=255,null=True, verbose_name='Park Adı')
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    capacity = models.IntegerField(null=True)
    empty_capacity = models.IntegerField(null=True)
    work_hours  = models.CharField(max_length=255,null=True)
    park_type = models.CharField(max_length=255,null=True)
    free_time = models.IntegerField(null=True)
    district = models.CharField(max_length=255,null=True)
    is_open = models.IntegerField(null=True)
    location = models.PointField(default='POINT(0.0 0.0)', blank=True, verbose_name='Konum')

    def __str__(self):
        return str(self.park_id)


    class Meta:
        verbose_name_plural = 'Parklar'

