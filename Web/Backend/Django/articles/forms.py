from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField()

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)
        # exclude = ('user')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)