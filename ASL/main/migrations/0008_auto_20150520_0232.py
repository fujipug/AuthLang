# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_content_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='country',
            field=models.CharField(default=b'Otro', max_length=200, choices=[(b'Mexico', b'Mexico'), (b'Colombia', b'Colombia'), (b'Espana', b'Espana'), (b'Argentina', b'Argentina'), (b'Chile', b'Chile'), (b'Costa Rica', b'Costa Rica'), (b'Peru', b'Peru'), (b'Venezuela', b'Venezuela'), (b'Guatemala', b'Guatemala'), (b'Republica Dominicana', b'Republica Dominicana'), (b'Otro', b'Otro')]),
        ),
        migrations.AlterField(
            model_name='content',
            name='difficulty',
            field=models.ForeignKey(to='main.Difficulty'),
        ),
        migrations.AlterField(
            model_name='difficulty',
            name='level',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='theme',
            name='theme',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
