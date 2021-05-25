from django import forms
from django.forms import widgets
from .models import Comment, Post

class CommentCreateForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=500)
    
    class Meta:
        model = Comment
        fields = ("comment",)

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=500)
    body = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control'}))
    class Meta:
        model = Post
        fields = ("title","body")