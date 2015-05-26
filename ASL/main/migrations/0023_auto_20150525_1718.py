# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_country_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='difficulty',
            field=models.ForeignKey(default=1, to='main.Difficulty'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='country',
            field=models.ForeignKey(to='main.Country'),
        ),
    ]
