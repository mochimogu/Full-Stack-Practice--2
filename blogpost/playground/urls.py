from django.urls import path, include
from . import views


#URL Configuration
urlpatterns = [
    path('home/', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('blogs/', views.getBlogs, name="getBlogs"),
    path('createBlogs/', views.createBlogs, name="createBlogs"),
    path('blogs/<int:index>', views.getPages, name="getPages"),
    path('searching/', views.searching, name="searching"),
    path('auth/<str:option>', views.authentication, name="user_auth")
]





