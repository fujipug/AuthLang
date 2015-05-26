# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_content_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentsubcategory',
            name='content',
        ),
        migrations.RemoveField(
            model_name='contentsubcategory',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='ContentSubcategory',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
