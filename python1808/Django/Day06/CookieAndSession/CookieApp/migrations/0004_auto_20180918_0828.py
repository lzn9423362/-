# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-18 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CookieApp', '0003_auto_20180918_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='passwd',
            field=models.CharField(max_length=32),
        ),
    ]
