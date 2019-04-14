# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-09 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carimageinfo',
            old_name='addtime',
            new_name='AddTime',
        ),
        migrations.RenameField(
            model_name='carimageinfo',
            old_name='adduser',
            new_name='AddUser',
        ),
        migrations.RenameField(
            model_name='carimageinfo',
            old_name='carid',
            new_name='CarId',
        ),
        migrations.RenameField(
            model_name='carimageinfo',
            old_name='carimageid',
            new_name='CarImageId',
        ),
        migrations.RenameField(
            model_name='carimageinfo',
            old_name='imageurl',
            new_name='ImageUrl',
        ),
        migrations.RenameField(
            model_name='carimageinfo',
            old_name='iscover',
            new_name='IsCover',
        ),
        migrations.RenameField(
            model_name='carimageinfo',
            old_name='lastedittime',
            new_name='LastEditTime',
        ),
        migrations.RenameField(
            model_name='carimageinfo',
            old_name='lastedituser',
            new_name='LastEditUser',
        ),
        migrations.RenameField(
            model_name='carimageinfo',
            old_name='status',
            new_name='Status',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='addtime',
            new_name='AddTime',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='adduser',
            new_name='AddUser',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='carid',
            new_name='CarId',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='carname',
            new_name='CarName',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='cartype',
            new_name='CarType',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='cargovolume',
            new_name='CargoVolume',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='fixprice',
            new_name='FixPrice',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='imageurl',
            new_name='ImageUrl',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='lastedittime',
            new_name='LastEditTime',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='lastedituser',
            new_name='LastEditUser',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='lengthwidthheight',
            new_name='LengthWidthHeight',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='load',
            new_name='Load',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='sort',
            new_name='Sort',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='status',
            new_name='Status',
        ),
        migrations.RenameField(
            model_name='carinfo',
            old_name='tips',
            new_name='Tips',
        ),
    ]
