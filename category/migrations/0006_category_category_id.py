# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_category_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Category'),
        ),
    ]
