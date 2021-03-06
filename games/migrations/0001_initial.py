# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 03:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import games.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=games.models.image_classification_upload_to, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ClassificationGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Classification')),
            ],
        ),
        migrations.CreateModel(
            name='DeveloperGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('NA', 'N/A'), ('DEV', 'Desarrollador'), ('PUB', 'Publicista'), ('PRO', 'Productor'), ('DIS', 'Dise\xf1ador')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('link', models.CharField(max_length=200)),
                ('image', models.ImageField(height_field='height_field', upload_to=games.models.image_game_featured_upload_to, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('show', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=games.models.image_game_upload_to, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('rate', models.IntegerField(default=0, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('release_date', models.DateField(null=True)),
                ('engine', models.CharField(blank=True, max_length=40, null=True)),
                ('type_game', models.CharField(choices=[('NA', 'N/A'), ('SHO', 'Shooter'), ('GEN', 'Generalidades'), ('FIG', 'Lucha'), ('BEU', 'Beat em up'), ('FPS', 'Disparos en primera persona'), ('TPS', 'Disparos en tercera persona'), ('EST', 'Estrateg\xeda'), ('SIM', 'Simulaci\xf3n'), ('SPO', 'Deporte'), ('RUN', 'Carreras'), ('ADV', 'Aventura')], default='NA', max_length=3)),
                ('genre', models.CharField(choices=[('NA', 'N/A'), ('ACT', 'Acci\xf3n'), ('ADV', 'Aventura'), ('HOR', 'Horror'), ('SCI', 'Ciencia Ficci\xf3n')], default='NA', max_length=3)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='LaunchGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('image', models.ImageField(height_field='height_field', upload_to=games.models.image_game_launch_upload_to, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=120)),
                ('excerpt', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=games.models.image_news_upload_to, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('link', models.CharField(max_length=200)),
                ('publish', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='PersonIndustry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=120)),
                ('occupation', models.CharField(choices=[('NA', 'N/A'), ('DEV', 'Desarrollador'), ('PUB', 'Publicista'), ('PRO', 'Productor'), ('DIS', 'Dise\xf1ador')], default='NA', max_length=3)),
                ('description', models.TextField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=games.models.image_image_upload_to, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=games.models.image_platform_upload_to, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Platform')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('url_youtube', models.CharField(max_length=200)),
                ('featured_image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=games.models.image_video_upload_to, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('type_video', models.CharField(choices=[('NA', 'N/A'), ('GPL', 'Gameplay'), ('WLK', 'Walkthrough'), ('DMO', 'Demo'), ('TRA', 'Trailer'), ('GID', 'Guia'), ('TRC', 'Trucos y Secretos')], default='NA', max_length=3)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
            ],
        ),
        migrations.AddField(
            model_name='gallerygame',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
        migrations.AddField(
            model_name='gallerygame',
            name='pictures',
            field=models.ManyToManyField(to='games.Picture'),
        ),
        migrations.AddField(
            model_name='gallerygame',
            name='videos',
            field=models.ManyToManyField(to='games.Video'),
        ),
        migrations.AddField(
            model_name='featuredgame',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
        migrations.AddField(
            model_name='developergame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
        migrations.AddField(
            model_name='developergame',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.PersonIndustry'),
        ),
        migrations.AddField(
            model_name='classificationgame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
    ]
