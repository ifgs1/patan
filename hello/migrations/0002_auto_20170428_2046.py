# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-28 20:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='design',
            name='designer',
        ),
        migrations.RemoveField(
            model_name='design',
            name='project',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Design',
        ),
        migrations.DeleteModel(
            name='Designer',
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
    ]
