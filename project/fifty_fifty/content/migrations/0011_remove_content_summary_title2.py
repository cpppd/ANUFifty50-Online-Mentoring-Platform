# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-11 10:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_content_summary_title2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content_summary',
            name='title2',
        ),
    ]
