# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20160521_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='street_line1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='street_line2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]