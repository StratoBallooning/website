# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 02:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='position',
            new_name='title',
        ),
    ]