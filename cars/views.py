from rest_framework import generics

from cars.serializers import CarDetailSerializer, CarListSerializer
from cars.models import Car
from cars.permission import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated,)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

# Need to make more view
