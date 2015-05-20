# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_difficulty_slugify_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difficulty',
            name='slugify_level',
            field=models.CharField(max_length=50, editable=False, blank=True),
        ),
    ]
