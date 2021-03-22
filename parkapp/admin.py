from django.contrib import admin
from .models import Park


class ParkAdmin(admin.ModelAdmin):
   list_display = ('id','park_name','location')

admin.site.register(Park,ParkAdmin)