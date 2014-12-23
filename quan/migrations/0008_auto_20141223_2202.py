# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quan', '0007_personalstatus_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ManyToManyField(to='quan.Group'),
            preserve_default=True,
        ),
    ]
