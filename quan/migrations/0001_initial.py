# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=10, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('lastname', models.CharField(max_length=10, verbose_name=b'\xe5\xa7\x93\xe6\xb0\x8f')),
                ('gender', models.CharField(max_length=10, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'male', b'\xe7\x94\xb7'), (b'female', b'\xe5\xa5\xb3')])),
                ('birth', models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5')),
                ('location', models.CharField(max_length=50, verbose_name=b'\xe6\x89\x80\xe5\x9c\xa8\xe5\x9c\xb0')),
                ('hometown', models.CharField(max_length=50, verbose_name=b'\xe5\xae\xb6\xe4\xb9\xa1')),
                ('company', models.CharField(max_length=50, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8')),
                ('job_position', models.CharField(max_length=20, verbose_name=b'\xe6\x89\x80\xe4\xbb\xbb\xe8\x81\x8c\xe4\xbd\x8d')),
                ('hobby', models.TextField(verbose_name=b'\xe7\x88\xb1\xe5\xa5\xbd')),
                ('skill', models.TextField(verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd')),
                ('acquaint_time', models.DateField(verbose_name=b'\xe8\xae\xa4\xe8\xaf\x86\xe6\x97\xb6\xe9\x97\xb4')),
                ('importance', models.CharField(max_length=10, verbose_name=b'\xe9\x87\x8d\xe8\xa6\x81\xe7\xa8\x8b\xe5\xba\xa6', choices=[(b'vip', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe9\x87\x8d\xe8\xa6\x81'), (b'important', b'\xe4\xb8\x80\xe8\x88\xac\xe9\x87\x8d\xe8\xa6\x81'), (b'normal', b'\xe6\x99\xae\xe9\x80\x9a')])),
                ('photo', models.ImageField(upload_to=b'', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87')),
                ('relationship', models.ForeignKey(to='quan.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
