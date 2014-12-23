# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quan', '0006_personalstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalstatus',
            name='person',
            field=models.ForeignKey(default=1, to='quan.Person'),
            preserve_default=False,
        ),
    ]
