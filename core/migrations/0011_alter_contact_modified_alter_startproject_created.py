# Generated by Django 4.1.5 on 2023-01-19 01:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_contact_email_alter_photogallery_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='startproject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 1, 16, 15, 262246, tzinfo=datetime.timezone.utc), verbose_name='created'),
        ),
    ]
