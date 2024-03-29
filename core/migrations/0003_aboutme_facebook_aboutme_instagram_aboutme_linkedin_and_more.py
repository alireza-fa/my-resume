# Generated by Django 4.1.5 on 2023-01-18 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_aboutme_resume_en_alter_startproject_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='facebook',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='facebook'),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='instagram',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='instagram'),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='linkedin',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='linkedin'),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='skype',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='skype'),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='twitter',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='twitter'),
        ),
        migrations.AlterField(
            model_name='startproject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 18, 6, 37, 41, 726927, tzinfo=datetime.timezone.utc), verbose_name='created'),
        ),
    ]
