# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-06 16:08
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20200106_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='videoblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('title', models.CharField(max_length=200)),
                ('clip', models.FileField(null=True, upload_to='user_videos/')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2020, 1, 6, 19, 8, 59, 425700), verbose_name='Дата')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 1, 6, 19, 8, 59, 422700), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 1, 6, 19, 8, 59, 424701), verbose_name='Дата'),
        ),
    ]