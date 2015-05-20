# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_content_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='country',
            field=models.CharField(default=b'Otro', max_length=200, choices=[(b'Mexico', b'Mexico'), (b'Colombia', b'Colombia'), (b'Espana', b'Espana'), (b'Otro', b'Otro')]),
        ),
    ]
