# Generated by Django 2.1.3 on 2019-07-15 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0057_auto_20190712_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='domain',
            field=models.CharField(default='www.toutiao.com', max_length=32),
        ),
        migrations.AlterField(
            model_name='news',
            name='explain',
            field=models.CharField(default='今日头条', max_length=32),
        ),
        migrations.AlterField(
            model_name='news',
            name='icon',
            field=models.CharField(default='//s3a.pstatp.com/toutiao/resource/ntoutiao_web/static/image/favicon_5995b44.ico ', max_length=32),
        ),
        migrations.AlterField(
            model_name='news',
            name='summary',
            field=models.CharField(default='戳我，查看详细信息>>>', max_length=128, null=True),
        ),
    ]
