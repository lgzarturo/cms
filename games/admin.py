from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from games.models import Game, Platform


@admin.register(Platform)
class PlatformAdmin(SummernoteModelAdmin):
    class Meta:
        model = Platform


@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):
    class Meta:
        model = Game
