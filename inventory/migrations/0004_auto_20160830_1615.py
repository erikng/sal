# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 15:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20160216_1756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventoryitem',
            options={'ordering': ['application', '-version']},
        ),
    ]