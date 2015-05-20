# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150520_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='theme',
            field=models.ForeignKey(default=1, to='main.Theme'),
        ),
        migrations.AddField(
            model_name='theme',
            name='country',
            field=models.ForeignKey(default=1, to='main.Country'),
        ),
        migrations.AlterField(
            model_name='difficulty',
            name='level',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='theme',
            name='difficulty',
            field=models.ForeignKey(default=1, to='main.Difficulty'),
        ),
    ]
