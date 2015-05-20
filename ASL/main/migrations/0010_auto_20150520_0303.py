# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150520_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='difficulty',
            field=models.ForeignKey(default=b'---', to='main.Difficulty'),
        ),
    ]
