# Generated by Django 4.1.5 on 2023-01-19 02:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_startproject_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsayaboutme',
            name='description_en',
            field=models.TextField(default='a', verbose_name='description english'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientsayaboutme',
            name='fullname_en',
            field=models.CharField(default='1', max_length=34, verbose_name='fullname english'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientsayaboutme',
            name='position_en',
            field=models.CharField(default='a', max_length=64, verbose_name='position english'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='startproject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 2, 3, 23, 412370, tzinfo=datetime.timezone.utc), verbose_name='created'),
        ),
    ]
