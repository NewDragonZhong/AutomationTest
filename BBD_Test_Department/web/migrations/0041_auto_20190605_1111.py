# Generated by Django 2.1.3 on 2019-06-05 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0040_auto_20190531_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pertestingtable',
            name='user_info',
        ),
        migrations.DeleteModel(
            name='PertestingTable',
        ),
    ]