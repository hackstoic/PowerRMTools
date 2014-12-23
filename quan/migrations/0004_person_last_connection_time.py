# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quan', '0003_auto_20141127_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='last_connection_time',
            field=models.DateField(default=datetime.datetime(2014, 11, 27, 8, 59, 36, 215000), verbose_name=b'\xe6\x9c\x80\xe8\xbf\x91\xe8\x81\x94\xe7\xb3\xbb\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=False,
        ),
    ]
