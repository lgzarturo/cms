from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from taggit_helpers.admin import TaggitTabularInline, TaggitListFilter, TaggitCounter

from games.models import Game, Platform, LaunchGame, FeaturedGame, News, Video, Picture, GalleryGame, PersonIndustry, \
    Classification, DeveloperGame, ClassificationGame, PlatformGame


@admin.register(Platform)
class PlatformAdmin(SummernoteModelAdmin):
    fields = ('name', 'image', 'description',)

    class Meta:
        model = Platform


class LaunchGameInline(admin.TabularInline):
    fields = ('image', 'date',)
    model = LaunchGame
    extra = 0
    max_num = 1


class VideoInline(admin.TabularInline):
    fields = ('title', 'url_youtube', 'featured_image', 'type_video')
    model = Video
    extra = 0


class PictureInline(admin.TabularInline):
    fields = ('title', 'excerpt', 'picture')
    model = Picture
    extra = 0


class DeveloperInline(admin.TabularInline):
    model = DeveloperGame
    extra = 0


class ClassificationInline(admin.TabularInline):
    model = ClassificationGame
    extra = 0


class PlatformInline(admin.TabularInline):
    model = PlatformGame
    extra = 0


@admin.register(Game)
class GameAdmin(TaggitCounter, SummernoteModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'rate', 'release_date', 'tags',)
        }),
        ('Opciones avanzadas', {
            'classes': ('collapse',),
            'fields': ('image', 'website', 'engine', 'type_game', 'genre',),
        }),
    )
    inlines = [LaunchGameInline, PictureInline, VideoInline, DeveloperInline, ClassificationInline, PlatformInline,
               TaggitTabularInline]
    list_filter = [TaggitListFilter, 'type_game', 'genre', ]
    list_display = ('name', 'release_date', 'type_game', 'genre', 'taggit_counter', )

    class Meta:
        model = Game


@admin.register(LaunchGame)
class LaunchGameAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'date', 'game',)

    class Meta:
        model = LaunchGame


@admin.register(FeaturedGame)
class FeaturedGameAdmin(admin.ModelAdmin):
    fields = ('title', 'link', 'image', 'description', 'game',)

    class Meta:
        model = FeaturedGame


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    fields = ('title', 'excerpt', 'content', 'image', 'link', 'publish', 'tags',)

    class Meta:
        model = News


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    fields = ('title', 'url_youtube', 'featured_image', 'type_video', 'game',)

    class Meta:
        model = Video


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    fields = ('title', 'excerpt', 'picture', 'game',)

    class Meta:
        model = Picture


@admin.register(GalleryGame)
class GalleryGameAdmin(admin.ModelAdmin):
    fields = ('title', 'pictures', 'videos', 'show', 'game',)

    class Meta:
        model = GalleryGame


@admin.register(PersonIndustry)
class PersonIndustryAdmin(SummernoteModelAdmin):
    fields = ('name', 'occupation', 'tags', 'description', 'nationality',)

    class Meta:
        model = PersonIndustry


@admin.register(Classification)
class ClassificationAdmin(SummernoteModelAdmin):
    fields = ('name', 'description', 'image')

    class Meta:
        model = Classification
