# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20150520_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='slug',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
