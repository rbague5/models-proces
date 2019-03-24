# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-22 18:13
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Botiga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nif', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('street', models.TextField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('city', models.TextField(default='')),
                ('zipCode', models.TextField(blank=True, null=True)),
                ('stateOrProvince', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('telephone', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Euro amount')),
                ('date', models.DateField(default=datetime.date.today)),
                ('origin', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('botiga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='carns', to='carnisseria.Botiga')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Precuinats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Euro amount')),
                ('date', models.DateField(default=datetime.date.today)),
                ('elaboration_date', models.DateField(default=datetime.date.today)),
                ('caducity_date', models.DateField(default=datetime.date.today)),
                ('botiga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='precuinats', to='carnisseria.Botiga')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
