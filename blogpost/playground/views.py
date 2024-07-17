from django.shortcuts import render, HttpResponse
# Create your views here.
#HTTP REQUESTS


def home(request):
    return render(request, "home.html")

def create(request):
    return render(request, "create.html")