# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('regNo', models.CharField(max_length=200)),
                ('clubName1', models.CharField(max_length=200)),
                ('clubName2', models.CharField(max_length=200)),
                ('clubName3', models.CharField(max_length=200)),
                ('clubName4', models.CharField(max_length=200)),
            ],
        ),
    ]
