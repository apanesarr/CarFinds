from django.urls import include, path, re_path
from . import views
urlpatterns = [
    path('api/v1/cars/',
        views.get_cars.as_view(),
        name =' get_cars'
    )
]