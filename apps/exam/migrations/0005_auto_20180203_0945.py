# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-03 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20180203_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='posted_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posted_quotes', to='exam.User'),
        ),
    ]