# Generated by Django 2.1.3 on 2018-11-30 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20181128_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spiderproduct',
            name='user_info',
        ),
    ]