# Generated by Django 4.1.5 on 2023-01-19 02:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 2, 25, 30, 653545, tzinfo=datetime.timezone.utc), verbose_name='date'),
        ),
    ]