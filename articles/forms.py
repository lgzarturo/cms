# coding=utf-8
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "image",
            "content",
            "draft",
            "publish",
        ]
        widgets = {
            "content": SummernoteWidget(),
        }


class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, label='Búsqueda')
