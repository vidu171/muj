# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 21:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170624_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 24, 21, 28, 34, 313306, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='end_time',
            field=models.DateTimeField(max_length=200),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_time',
            field=models.DateTimeField(max_length=200),
        ),
    ]
