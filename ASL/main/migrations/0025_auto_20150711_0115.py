# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_content_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='contentcategory',
            name='content',
        ),
        migrations.DeleteModel(
            name='ContentCategory',
        ),
    ]
