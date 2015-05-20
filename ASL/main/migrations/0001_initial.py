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
                ('country', models.CharField(max_length=200)),
                ('video', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
