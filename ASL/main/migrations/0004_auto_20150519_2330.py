# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_content_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='video',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
