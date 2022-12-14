from django.urls import path
from .views import get_family,get_animal

urlpatterns = [
    path('famille/<int:x>', get_family,name='my-family'),
    path('animal/<int:x>',get_animal,name='animal-id')
]