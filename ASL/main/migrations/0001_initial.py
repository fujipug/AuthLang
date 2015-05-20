# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('vocab', models.CharField(max_length=200, null=True, blank=True)),
                ('video', models.URLField()),
                ('difficulty', models.CharField(default=b'Otro', max_length=200, choices=[(b'Facil', b'Facil'), (b'Mediano', b'Mediano'), (b'Duro', b'Duro'), (b'Otro', b'Otro')])),
                ('country', models.CharField(default=b'Otro', max_length=200, choices=[(b'Mexico', b'Mexico'), (b'Colombia', b'Colombia'), (b'Espana', b'Espana'), (b'Otro', b'Otro')])),
            ],
        ),
    ]
