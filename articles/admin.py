from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_display_links = ["updated"]
    list_filter = ["timestamp", "updated"]
    search_fields = ["title"]
    list_editable = ["title"]

    class Meta:
        model = Article
