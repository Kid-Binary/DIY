# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-20 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20170120_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='centresubpage',
            name='slug',
            field=models.SlugField(default='-', editable=False, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='centresubpage',
            name='headline_uk',
            field=models.CharField(max_length=150, verbose_name='Назва сторінки'),
        ),
    ]
