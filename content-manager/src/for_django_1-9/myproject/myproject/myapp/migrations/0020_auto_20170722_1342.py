# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20170721_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Week',
            field=models.CharField(choices=[('Week_1', 'Week_1'), ('Week_2', 'Week_2'), ('Week_2', 'Week_3'), ('Week_2', 'Week_4')], default='Week_1', max_length=10),
        ),
    ]