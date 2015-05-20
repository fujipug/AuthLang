# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20150520_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='difficulty',
            name='slugify_level',
        ),
        migrations.AddField(
            model_name='difficulty',
            name='slug',
            field=models.CharField(unique=True, max_length=50, blank=True),
        ),
    ]
