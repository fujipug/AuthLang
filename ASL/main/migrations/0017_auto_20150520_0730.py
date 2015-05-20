# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20150520_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difficulty',
            name='slug',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
