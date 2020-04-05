from django import forms
from .models import Post

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100)
    subject = forms.CharField(max_length = 100)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title", "text", "profile_pic")