# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20150520_0804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(unique=True, max_length=200)),
                ('slug', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_type', models.CharField(unique=True, max_length=200)),
                ('slug', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContentCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(to='main.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ContentSubcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcategory', models.CharField(unique=True, max_length=200)),
                ('slug', models.CharField(max_length=200, blank=True)),
                ('category', models.ForeignKey(default=1, to='main.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='theme',
            name='country',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='content',
            name='country',
        ),
        migrations.RemoveField(
            model_name='content',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='content',
            name='theme',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Difficulty',
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.AddField(
            model_name='contentsubcategory',
            name='content',
            field=models.ForeignKey(to='main.Content'),
        ),
        migrations.AddField(
            model_name='contentsubcategory',
            name='subcategory',
            field=models.ForeignKey(to='main.Subcategory'),
        ),
        migrations.AddField(
            model_name='contentcategory',
            name='content',
            field=models.ForeignKey(to='main.Content'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_type',
            field=models.ForeignKey(default=1, to='main.CategoryType'),
        ),
    ]
