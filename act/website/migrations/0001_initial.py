# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-19 13:47
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uk', models.CharField(max_length=100, verbose_name='Назва діяльності')),
                ('icon', models.CharField(max_length=30, verbose_name='Іконка')),
            ],
            options={
                'verbose_name_plural': '          Види діяльності',
                'db_table': 'website_activities',
                'verbose_name': 'Вид діяльності',
            },
        ),
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description_uk', models.CharField(max_length=500, verbose_name='Короткий опис')),
            ],
            options={
                'verbose_name_plural': '        Центри',
                'db_table': 'website_centres',
                'verbose_name': 'Центр',
            },
        ),
        migrations.CreateModel(
            name='CentreSubpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline_uk', models.CharField(max_length=100, verbose_name='Назва сторінки')),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centres_subpages', to='website.Centre')),
            ],
            options={
                'verbose_name_plural': '       Підсторінки Центрів',
                'db_table': 'website_centres_subpages',
                'verbose_name': 'Підсторінка Центру',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='cities/photos/', verbose_name='Фотографія')),
                ('photo_thumb', models.ImageField(null=True, upload_to='cities/photos/thumbs/', verbose_name='Фотографія')),
                ('name_uk', models.CharField(max_length=100, unique=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name_plural': '         Міста',
                'db_table': 'website_cities',
                'verbose_name': 'Місто',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=19, verbose_name='Телефон')),
                ('address_uk', models.CharField(blank=True, max_length=300, null=True, verbose_name='Адреса')),
                ('centre', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Centre')),
            ],
            options={
                'verbose_name_plural': '      Контакти',
                'db_table': 'website_contacts',
                'verbose_name': 'Контакт',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='events/images/', verbose_name='Головне зображення')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата та час події')),
                ('title_uk', models.CharField(max_length=200, verbose_name='Назва')),
                ('content_uk', ckeditor.fields.RichTextField(verbose_name='Контент')),
                ('is_active', models.BooleanField(default=True, verbose_name='Відображається')),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name_plural': '  Події',
                'verbose_name': 'Подія',
                'ordering': ('created_at',),
                'db_table': 'website_events',
            },
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uk', models.CharField(max_length=100, unique=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name_plural': '   Категорії подій',
                'db_table': 'website_events_categories',
                'verbose_name': 'Категорія події',
            },
        ),
        migrations.CreateModel(
            name='IntroContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('headline_uk', models.CharField(max_length=200, verbose_name='Вступна фраза')),
            ],
            options={
                'verbose_name_plural': '             Інтро',
                'db_table': 'website_content_intro',
                'verbose_name': 'Інтро',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='participants/photos/', verbose_name='Фотографія')),
                ('photo_thumb', models.ImageField(null=True, upload_to='participants/photos/thumbs/', verbose_name='Фотографія')),
                ('position_uk', models.CharField(max_length=100, verbose_name='Посада')),
                ('name_uk', models.CharField(max_length=200, verbose_name='Імʼя')),
                ('surname_uk', models.CharField(max_length=200, verbose_name='Прізвище')),
                ('centre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participants', to='website.Centre')),
            ],
            options={
                'verbose_name_plural': '      Співробітники',
                'db_table': 'website_participants',
                'verbose_name': 'Співробітник',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/images/', verbose_name='Головне зображення')),
                ('title_uk', models.CharField(max_length=200, unique=True, verbose_name='Назва')),
                ('started_at', models.DateField(auto_now_add=True, verbose_name='Дата початку')),
                ('content_uk', ckeditor.fields.RichTextField(verbose_name='Контент')),
                ('is_active', models.BooleanField(default=True, verbose_name='Відображається')),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name_plural': '    Проекти',
                'verbose_name': 'Проект',
                'ordering': ('started_at',),
                'db_table': 'website_projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uk', models.CharField(max_length=100, unique=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name_plural': '     Напрямки проектів',
                'db_table': 'website_projects_areas',
                'verbose_name': 'Напрямок проекту',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва мережі')),
                ('link', models.URLField(max_length=300, verbose_name='Посилання')),
                ('icon', models.CharField(max_length=30, verbose_name='Іконка')),
            ],
            options={
                'verbose_name_plural': '           Соціальні мережі',
                'db_table': 'website_socials',
                'verbose_name': 'Соціальна мережа',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='sponsors/logos/', verbose_name='Логотип')),
                ('title_uk', models.CharField(max_length=100, verbose_name='Назва організації')),
                ('link', models.URLField(max_length=300, verbose_name='Посилання')),
            ],
            options={
                'verbose_name_plural': '            Донори',
                'db_table': 'website_sponsors',
                'verbose_name': 'Донор',
            },
        ),
        migrations.CreateModel(
            name='Worksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300, verbose_name='ПІБ')),
                ('residence', models.CharField(max_length=500, verbose_name='Місце проживання')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=19, verbose_name='Телефон')),
                ('personal_link', models.URLField(blank=True, null=True, verbose_name='Персональна сторінка')),
                ('problem', models.BooleanField(verbose_name='Бажаєте повідомити про проблему?')),
                ('problem_description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Із якою проблемою Вам довелося зіштовхнутися?')),
                ('activity', models.BooleanField(verbose_name='Чи бажаєте Ви долучитись до «ДІЙ!»?')),
                ('activity_description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='У якій діяльності в рамках «ДІЙ!» ви би хотіли взяти участь?')),
            ],
            options={
                'verbose_name_plural': '      Анкети',
                'db_table': 'website_worksheet',
                'verbose_name': 'Анкета',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='website.ProjectArea'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='website.EventCategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='website.Project'),
        ),
        migrations.AddField(
            model_name='centre',
            name='city',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.City'),
        ),
        migrations.AddField(
            model_name='centre',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='centres', to='website.Event'),
        ),
        migrations.AddField(
            model_name='centre',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='centres', to='website.Project'),
        ),
    ]
