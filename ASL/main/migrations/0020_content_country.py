# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20150524_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='country',
            field=models.ForeignKey(default=2, to='main.Category'),
            preserve_default=False,
        ),
    ]
