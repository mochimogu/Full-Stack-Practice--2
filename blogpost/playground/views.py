from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogsSerializer
from .models import BlogPost
from .forms import BlogForm
from .forms import SearchForm
# Create your views here.
#HTTP REQUESTS


def home(request):
    search = SearchForm()
    return render(request, "home.html", {'search' : search})

def create(request):
    form = BlogForm()
    search = SearchForm()  
    return render(request, "create.html", { 'form' : form, 'search' : search})

@api_view(['GET'])
def getBlogs(request):
    items = BlogPost.objects.all()
    search = SearchForm()  
    serial = BlogsSerializer(items, many=True)

    return render(request, "blogs.html", {'data' : serial.data, 'search' : search})

@api_view(['GET'])
def getPages(request, index):
    search = SearchForm()  
    items = get_object_or_404(BlogPost, id=index)
    
    return render(request, "pages.html", {'data' : items, 'search' : search})


@api_view(['GET'])
def searching(request):
    search = SearchForm()
    if request.method == "GET" and "query" in request.GET:
        searching = SearchForm(request.GET)
        if searching.is_valid():
            word = searching.cleaned_data['query']
            print(word)
            searchResults = BlogPost.objects.filter(title__icontains=word) | BlogPost.objects.filter(blog__icontains=word)
            print(searchResults)

    return render(request, "search.html", { 'data' : searchResults, 'search' : search})


@api_view(['POST'])
def createBlogs(request):
    
    if request.method == "POST":
        
        form = BlogForm(request.POST)
        if form.is_valid():
            # Process the data
            name = form.cleaned_data['title']
            description = form.cleaned_data['blog']
            print(name)
            print(description)
            
            sending = {
                'title' : name,
                'blog' : description
            }
            
            serial = BlogsSerializer(data=request.data)
            if serial.is_valid():
                serial.save();
            
            return redirect("/playground/blogs")
    else:
        form = BlogForm()  
        
    return render(request, 'create.html', {'form' : form})


@api_view(['GET'])
def authentication(request, option):
    
    return render(request, "auth.html", { 'option' : option})
