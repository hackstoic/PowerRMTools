# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quan', '0005_auto_20141127_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('update_time', models.DateField(verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('status_desc', models.CharField(max_length=1000, verbose_name=b'\xe5\x8a\xa8\xe6\x80\x81\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
