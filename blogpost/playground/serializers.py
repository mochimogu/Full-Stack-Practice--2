# myapp/serializers.py
from rest_framework import serializers
from .models import BlogPost

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
