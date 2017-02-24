from django.contrib import admin

from newsletters.models import Join


@admin.register(Join)
class JoinAdmin(admin.ModelAdmin):
    list_display = ["email", 'ip_address', "timestamp", "updated"]
    list_display_links = ["updated"]
    list_filter = ["timestamp", "updated"]
    search_fields = ["email"]

    class Meta:
        model = Join
