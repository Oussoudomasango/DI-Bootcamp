from django.urls import path
from .views import family,animals
#,animals

urlpatterns = [
    path("family/<int:x>/", family, name='family'),
    path('animals/<int:x>/', animals, name='Animals')
]