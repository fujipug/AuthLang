# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150520_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='country',
            field=models.ForeignKey(default=1, to='main.Country'),
        ),
        migrations.AlterField(
            model_name='content',
            name='difficulty',
            field=models.ForeignKey(default=1, to='main.Difficulty'),
        ),
    ]
