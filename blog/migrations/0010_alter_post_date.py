# Generated by Django 4.1.5 on 2023-01-19 01:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 1, 10, 9, 189377, tzinfo=datetime.timezone.utc), verbose_name='date'),
        ),
    ]
