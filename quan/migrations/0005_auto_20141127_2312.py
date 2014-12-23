# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quan', '0004_person_last_connection_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='qq',
            field=models.CharField(default=0, max_length=15, verbose_name=b'QQ\xe5\x8f\xb7', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='wechat',
            field=models.CharField(default=0, max_length=25, verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1\xe5\x8f\xb7', blank=True),
            preserve_default=False,
        ),
    ]
