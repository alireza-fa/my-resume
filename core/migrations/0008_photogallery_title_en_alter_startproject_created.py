# Generated by Django 4.1.5 on 2023-01-19 00:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_photogallery_title_alter_startproject_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='photogallery',
            name='title_en',
            field=models.CharField(default='title english', max_length=200, verbose_name='title english'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='startproject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 0, 39, 12, 229366, tzinfo=datetime.timezone.utc), verbose_name='created'),
        ),
    ]
