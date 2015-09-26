# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=18)),
                ('breed', models.CharField(max_length=20)),
                ('colour', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'post_pictures', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField(max_length=800)),
                ('type', models.CharField(max_length=20)),
                ('state', models.BooleanField(default=True)),
                ('date', models.DateField(blank=True)),
                ('user_post', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=128)),
                ('user_profile', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='post_picture',
            field=models.ForeignKey(to='principal.Post'),
        ),
        migrations.AddField(
            model_name='dog',
            name='post_dog',
            field=models.ForeignKey(to='principal.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post_comment',
            field=models.ForeignKey(to='principal.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
