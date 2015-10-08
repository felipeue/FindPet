# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default=datetime.datetime(2015, 9, 25, 19, 31, 33, 11582, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2015, 9, 25, 19, 31, 43, 867013, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
    ]
