# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-30 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0028_profile_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='university',
            field=models.CharField(choices=[('', '-'), ('ANU', 'The Australian National University')], max_length=100, null=True),
        ),
    ]
