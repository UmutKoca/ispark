from django.http import request
from rest_framework import serializers
from parkapp.api.serializers import ParkSerializer, ParkUpdateCreateSerializer
from rest_framework.generics import (CreateAPIView, 
                                    DestroyAPIView, 
                                    ListAPIView, 
                                    RetrieveAPIView, RetrieveUpdateAPIView, 
                                    UpdateAPIView,)

from parkapp.models import Park 
from rest_framework.permissions import(
    IsAuthenticated,
    IsAdminUser
)

# Custom permission
from parkapp.api.permissions import IsOwner

class ParkListAPIView(ListAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer

class ParkDetailAPIView(RetrieveAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
    lookup_field = 'pk'

class ParkDeleteAPIView(DestroyAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(user = self.request.user)

class ParkUpdateAPIView(UpdateAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkUpdateCreateSerializer
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(user = self.request.user)

class PostCreateAPIView(CreateAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkUpdateCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)