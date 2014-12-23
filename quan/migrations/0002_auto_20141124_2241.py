# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=datetime.datetime(2014, 11, 24, 22, 41, 28, 384000), max_length=75, verbose_name=b'\xe7\x94\xb5\xe5\xad\x90\xe9\x82\xae\xe7\xae\xb1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(default=datetime.datetime(2014, 11, 24, 22, 41, 37, 939000), max_length=15, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81'),
            preserve_default=False,
        ),
    ]
