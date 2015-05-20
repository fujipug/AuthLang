# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_difficulty_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
