# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150520_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='difficulty',
            name='slugify_level',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
