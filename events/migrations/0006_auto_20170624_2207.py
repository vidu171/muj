# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 22:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20170624_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 24, 22, 7, 29, 342214, tzinfo=utc)),
        ),
    ]