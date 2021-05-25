from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=500)
    
    class Meta:
        model = Comment
        fields = ("comment",)
