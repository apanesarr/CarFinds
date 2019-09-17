from rest_framework import status
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .models import Car
from .serializers import CarSerializer
from .permissions import IsAuthenticated

class get_cars(ListCreateAPIView):
    permission_class = IsAuthenticated
    serializer_class = CarSerializer
    pagination_class = PageNumberPagination
    search_fields = ['name', 'vendor']
    filter_backends = (filters.SearchFilter,)
    queryset = Car.objects.all()

