# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-10 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginTokenInfo',
            fields=[
                ('LoginTokenId', models.AutoField(db_column='LoginTokenId', primary_key=True, serialize=False, verbose_name='tokenID')),
                ('DriverId', models.IntegerField(blank=True, db_column='DriverId', null=True, verbose_name='司机ID')),
                ('CustomerId', models.IntegerField(blank=True, db_column='CustomerId', null=True, verbose_name='客户ID')),
                ('LoginToken', models.CharField(blank=True, db_column='LoginToken', max_length=32, null=True, verbose_name='token信息')),
                ('LoginTokenExpireDate', models.DateTimeField(db_column='LoginTokenExpireDate', verbose_name='过期时间')),
            ],
            options={
                'db_table': 'c_logintokeninfo',
                'verbose_name': 'token信息',
                'verbose_name_plural': 'token信息',
            },
        ),
    ]
