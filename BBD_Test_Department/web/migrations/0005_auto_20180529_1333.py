# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-29 05:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20171205_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='news',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_info',
        ),
        migrations.RemoveField(
            model_name='news',
            name='nt',
        ),
        migrations.RemoveField(
            model_name='news',
            name='user',
        ),
        migrations.DeleteModel(
            name='SendMsg',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='NewsType',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]