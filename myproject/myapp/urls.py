from django.urls import path
from .views import fruits
urlpatterns = [
    path('fruits/',fruits),
    
]