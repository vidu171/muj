# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 21:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170624_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 24, 21, 27, 29, 441429, tzinfo=utc)),
        ),
    ]
