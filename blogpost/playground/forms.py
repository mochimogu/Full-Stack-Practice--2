from django import forms



class BlogForm(forms.Form):
    title = forms.CharField(max_length=20)
    blog = forms.CharField(widget=forms.Textarea)
