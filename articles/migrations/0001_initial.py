# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 14:17
from __future__ import unicode_literals

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=articles.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
