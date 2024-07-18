from django.urls import path, include
from . import views


#URL Configuration
urlpatterns = [
    path('home/', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('get/', views.get, name="get"),
    path('blogs/', views.getBlogs, name="getBlogs"),
    path('createBlogs/', views.createBlogs, name="createBlogs"),

]





