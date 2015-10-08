# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20151006_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_profile',
            new_name='user',
        ),
    ]
