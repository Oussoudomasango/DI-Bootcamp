from django.urls import path
from .views import index,posts,signup
urlpatterns = [
    path('homepage/',index,name="homepage"),
    path('posts/',posts,name="posts"),
    path('signup/',signup,name="signup")
]