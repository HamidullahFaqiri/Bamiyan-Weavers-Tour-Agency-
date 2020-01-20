# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-06 18:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200106_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 1, 6, 21, 40, 47, 611937), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 1, 6, 21, 40, 47, 611937), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='videoblog',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 1, 6, 21, 40, 47, 612937), verbose_name='Дата'),
        ),
    ]