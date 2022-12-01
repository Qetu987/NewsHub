from django import forms
from blog.models import Post, Like



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "poster")

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ("post",)