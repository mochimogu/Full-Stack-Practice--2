from django.urls import path, include
from . import views


#URL Configuration
urlpatterns = [
    path('home/', views.home, name="home"),
    path('create/', views.create, name="create")
]





