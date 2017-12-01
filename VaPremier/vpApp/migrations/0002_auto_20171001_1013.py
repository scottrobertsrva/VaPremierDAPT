# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fluexponly',
            name='id',
        ),
        migrations.RemoveField(
            model_name='flurelatedexp',
            name='id',
        ),
        migrations.RemoveField(
            model_name='flushotdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='fluexponly',
            name='claim_num',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='flurelatedexp',
            name='claim_num',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='flushotdata',
            name='claim_num',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]