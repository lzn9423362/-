# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-13 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20180913_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
