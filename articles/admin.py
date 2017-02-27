from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_display_links = ["updated"]
    list_filter = ["timestamp", "updated"]
    search_fields = ["title"]
    list_editable = ["title"]

    class Meta:
        model = Article
