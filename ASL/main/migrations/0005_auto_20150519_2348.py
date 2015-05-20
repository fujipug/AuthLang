# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150519_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='difficulty',
            field=models.CharField(default=b'Otro', max_length=200, choices=[(b'Principante', b'Principante'), (b'Intermedio', b'Intermedio'), (b'Dificil', b'Dificil'), (b'Otro', b'Otro')]),
        ),
    ]
