# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20150525_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='categories',
            field=models.ManyToManyField(to='main.Category'),
        ),
    ]
