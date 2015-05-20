# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150520_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='difficulty',
            name='level',
            field=models.CharField(default=b'---', unique=True, max_length=200),
        ),
    ]
