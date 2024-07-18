from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=20)
    blog = models.TextField(max_length=300)



