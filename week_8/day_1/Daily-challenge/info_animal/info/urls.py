from django.urls import path
from .views import listPeople,only

urlpatterns = [
    path('people/', listPeople,name="list people"),
    path('only/<int:id>',only,name="only_file")
]