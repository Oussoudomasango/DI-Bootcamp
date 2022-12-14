
from django.urls import path
from .views import AddGif,homepage,AddCategory,categorys
urlpatterns = [
    path('homepage/',homepage,name="homepage"),
    path('addNewGif/', AddGif.as_view(), name='addgif'),
    path('addNewCategory/',AddCategory.as_view(),name='category'),
    path('category/<int:id>/', categorys, name='categorys'),
    
]