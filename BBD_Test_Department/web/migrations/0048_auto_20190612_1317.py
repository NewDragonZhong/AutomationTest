# Generated by Django 2.1.3 on 2019-06-12 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0047_auto_20190612_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pertestingserverstable',
            name='user_info',
        ),
        migrations.DeleteModel(
            name='PertestingServersTable',
        ),
    ]