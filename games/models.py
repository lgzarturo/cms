from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify


def image_platform_upload_to(instance, filename):
    title = instance.name
    slug = slugify(title)
    filename = slugify(filename)
    return "platform/%s/%s" % (slug, filename)


class Platform(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to=image_platform_upload_to,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)


def image_game_upload_to(instance, filename):
    title = instance.name
    slug = slugify(title)
    filename = slugify(filename)
    return "platform/%s/%s" % (slug, filename)


class Game(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to=image_game_upload_to,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    website = models.URLField()
    release_date = models.DateField()
    engine = models.CharField(max_length=40)
    type_game = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)


