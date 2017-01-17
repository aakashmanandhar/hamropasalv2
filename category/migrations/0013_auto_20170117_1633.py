# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0012_auto_20170114_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='category.Category', verbose_name='Parent'),
        ),
    ]
