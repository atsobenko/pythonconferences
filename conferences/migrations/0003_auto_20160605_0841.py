# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_conference_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='participants',
            field=models.ManyToManyField(to='conferences.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='conferences.Company'),
        ),
    ]
