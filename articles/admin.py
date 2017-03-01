from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from taggit_helpers.admin import TaggitCounter
from taggit_helpers.admin import TaggitListFilter

from .models import Article


@admin.register(Article)
class ArticleAdmin(TaggitCounter, SummernoteModelAdmin):
    list_display = ["title", "timestamp", "updated", "taggit_counter"]
    list_display_links = ["updated"]
    list_filter = ["timestamp", "updated", TaggitListFilter]
    search_fields = ["title"]
    list_editable = ["title"]

    class Meta:
        model = Article
