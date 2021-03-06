# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('trigrame', models.CharField(default='AAA', max_length=3)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('create_date', models.DateField()),
                ('slug', models.SlugField(default='ERROR_SLUGIFY', max_length=40)),
            ],
        ),
    ]
