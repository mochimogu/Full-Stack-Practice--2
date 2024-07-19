from django import forms
from . import models

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = ['title', 'blog']

class SearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=50)