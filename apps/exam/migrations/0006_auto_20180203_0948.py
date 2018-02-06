# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-03 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20180203_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='posted_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posted_quotes', to='exam.User'),
        ),
    ]