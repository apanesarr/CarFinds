from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .models import Car
from .serializers import CarSerializer
from .permissions import IsAuthenticated

class get_cars(ListCreateAPIView):
    permission_class = IsAuthenticated
   
    def get(self, request):
        cars = Car.objects.all()
        serialzer = CarSerializer(cars, many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)
