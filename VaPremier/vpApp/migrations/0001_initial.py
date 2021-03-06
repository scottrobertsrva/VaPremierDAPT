# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FluExpOnly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_num', models.CharField(blank=True, max_length=8, null=True)),
                ('member_id', models.CharField(blank=True, max_length=10, null=True)),
                ('claim_date', models.DateField(blank=True, null=True)),
                ('fiscal_year', models.CharField(blank=True, max_length=4, null=True)),
                ('month', models.DateField(blank=True, null=True)),
                ('paid_amt', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('l_d_code', models.CharField(blank=True, max_length=50, null=True)),
                ('l_d_desc', models.CharField(blank=True, max_length=500, null=True)),
                ('exptype', models.CharField(blank=True, db_column='expType', max_length=30, null=True)),
                ('age', models.CharField(blank=True, max_length=3, null=True)),
                ('plan', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('city_county', models.CharField(blank=True, max_length=50, null=True)),
                ('fips', models.CharField(blank=True, max_length=5, null=True)),
                ('place', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'flu_exp_only',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FluRelatedExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_num', models.CharField(blank=True, max_length=8, null=True)),
                ('member_id', models.CharField(blank=True, max_length=10, null=True)),
                ('claim_date', models.DateField(blank=True, null=True)),
                ('fiscal_year', models.CharField(blank=True, max_length=4, null=True)),
                ('month', models.DateField(blank=True, null=True)),
                ('paid_amt', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cat', models.CharField(blank=True, max_length=20, null=True)),
                ('cat2', models.CharField(blank=True, max_length=40, null=True)),
                ('cat3', models.CharField(blank=True, max_length=40, null=True)),
                ('age', models.CharField(blank=True, max_length=3, null=True)),
                ('plan', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('city_county', models.CharField(blank=True, max_length=50, null=True)),
                ('fips', models.CharField(blank=True, max_length=5, null=True)),
                ('place', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'flu_related_exp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FluShotData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_num', models.CharField(blank=True, max_length=8, null=True)),
                ('member_id', models.CharField(blank=True, max_length=10, null=True)),
                ('claim_date', models.DateField(blank=True, null=True)),
                ('fiscal_year', models.CharField(blank=True, max_length=4, null=True)),
                ('month', models.DateField(blank=True, null=True)),
                ('paid_amt', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('l_d_code', models.CharField(blank=True, max_length=50, null=True)),
                ('l_d_desc', models.CharField(blank=True, max_length=500, null=True)),
                ('exptype', models.CharField(blank=True, db_column='expType', max_length=30, null=True)),
                ('age', models.CharField(blank=True, max_length=3, null=True)),
                ('plan', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('city_county', models.CharField(blank=True, max_length=50, null=True)),
                ('fips', models.CharField(blank=True, max_length=5, null=True)),
                ('place', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'flu_shot_data',
                'managed': True,
            },
        ),
    ]
