# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-03 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_auto_20190103_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='is_menu',
            field=models.BooleanField(verbose_name='是否是菜单'),
        ),
    ]
