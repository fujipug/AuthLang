# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20150520_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.CharField(unique=True, max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='slug',
            field=models.CharField(unique=True, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='difficulty',
            name='slug',
            field=models.CharField(unique=True, max_length=200, blank=True),
        ),
    ]
