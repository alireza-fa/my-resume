# Generated by Django 4.1.5 on 2023-01-19 00:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 0, 38, 40, 720757, tzinfo=datetime.timezone.utc), verbose_name='date'),
        ),
    ]