from django.urls import path
from .views import phonenumber,name

urlpatterns = [
    path("phonenumber/<str:number>/", phonenumber, name="my phone number"),
    path("name/<str:nom>/",name, name="name")
]