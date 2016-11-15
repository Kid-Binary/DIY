# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(max_length=100, verbose_name='Роутінг')),
                ('title_uk', models.CharField(max_length=100, verbose_name='Назва сторінки')),
                ('description_uk', models.CharField(max_length=250, verbose_name='Опис сторінки')),
                ('robots', models.CharField(max_length=100, verbose_name='Інформація для ботів')),
            ],
            options={
                'verbose_name_plural': 'Метадані',
                'verbose_name': 'Метадані',
            },
        ),
    ]
