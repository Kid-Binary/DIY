# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20161128_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centre',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='centres', to='website.Event'),
        ),
        migrations.AlterField(
            model_name='centre',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='centres', to='website.Project'),
        ),
    ]
