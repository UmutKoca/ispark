from django.urls import path
from parkapp.api.views import (ParkDeleteAPIView, 
                               ParkDetailAPIView, 
                               ParkListAPIView, 
                               ParkUpdateAPIView, 
                               PostCreateAPIView)

urlpatterns = [
    path('list', ParkListAPIView.as_view(),name='list'),
    path('detail/<pk>', ParkDetailAPIView.as_view(),name='detail'),
    path('update/<pk>', ParkUpdateAPIView.as_view(),name='update'),
    path('delete/<pk>', ParkDeleteAPIView.as_view(),name='delete'),
    path('create/', PostCreateAPIView.as_view(),name='delete')
]
