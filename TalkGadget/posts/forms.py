from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        fields = ('author','title', 'text', 'category')
        model = Post
