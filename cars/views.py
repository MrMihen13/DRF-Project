from rest_framework import generics
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.response import Response
# from rest_framework.views import APIView

from cars.serializers import CarDetailSerializer, CarListSerializer
from cars.models import Car
# from cars.permission import IsOwnerOrReadOnly


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
    permission_classes = (IsAuthenticated,)


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser, IsAuthenticated,)

# Need to make more view
