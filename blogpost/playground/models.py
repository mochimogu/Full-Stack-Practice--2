from django.db import models

# Create your models here.

class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    blog = models.TextField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)



