# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productfeatured_make_image_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfeatured',
            name='text_css_color',
            field=models.CharField(blank=True, default='#', max_length=7, null=True),
        ),
    ]
