from django import forms

from blog.models import Post


class CreatePostForm(forms.ModelForm):
    """Form for creating a new post"""
    """to control the generic views"""

    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'author', 'post_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-content', 'placeholder': 'Enter title'}),
            'body': forms.Textarea(attrs={'class': 'form-content'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'post_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
