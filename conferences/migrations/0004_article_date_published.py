# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 08:52
from __future__ import unicode_literals
from datetime import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0003_auto_20160605_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(default=datetime.now()),
            preserve_default=False,
        ),
    ]