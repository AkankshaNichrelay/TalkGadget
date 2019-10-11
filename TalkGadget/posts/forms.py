from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'text', 'category')
        model = Post

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
