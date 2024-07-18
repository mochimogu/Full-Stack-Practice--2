from django.shortcuts import render, HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogsSerializer
from .models import BlogPost
from .forms import BlogForm

# Create your views here.
#HTTP REQUESTS


def home(request):
    return render(request, "home.html")

def create(request):
    return render(request, "create.html")

def get(request):
    items = BlogPost.objects.all()
    print(items)
    return render(request, "home.html", {'list' : items})

@api_view(['GET'])
def getBlogs(request):
    items = BlogPost.objects.all()
    # print(BlogPost.objects.all())
    serial = BlogsSerializer(items, many=True)

    return render(request, "blogs.html", {'data' : serial.data})

@api_view(['POST'])
def createBlogs(request):
    
    # serial = BlogsSerializer(data=request.data)
    # if serial.is_valid():
    #     serial.save()
    
    # return Response(serial.data)
    if request.method == "POST":
        
        form = BlogForm(request.POST)
        # print(form)
        if form.is_valid():
            # Process the data
            name = form.cleaned_data['title']
            description = form.cleaned_data['blog']
            print(name)
            print(description)
            
            return render(request, 'create.html', {'results' : "successful"})
        
    return render(request, 'create.html', {'results' : "successful"})
