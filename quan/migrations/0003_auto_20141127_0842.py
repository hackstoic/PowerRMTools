# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quan', '0002_auto_20141124_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='relationship',
            new_name='group',
        ),
    ]
