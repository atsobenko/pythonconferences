# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0002_company_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]