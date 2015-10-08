# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import geoposition.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20150925_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='position',
            field=geoposition.fields.GeopositionField(default=datetime.datetime(2015, 9, 25, 20, 1, 41, 438990, tzinfo=utc), max_length=42),
            preserve_default=False,
        ),
    ]
