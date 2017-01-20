# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-20 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0002_auto_20170119_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opengraph',
            name='metadata',
        ),
        migrations.AlterField(
            model_name='twittercard',
            name='metadata',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='twitter_card', to='metadata.Metadata'),
        ),
        migrations.DeleteModel(
            name='OpenGraph',
        ),
    ]