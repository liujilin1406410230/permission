# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-03 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20190103_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='is_menu',
            field=models.BooleanField(default='False', verbose_name='是否是菜单'),
        ),
    ]
