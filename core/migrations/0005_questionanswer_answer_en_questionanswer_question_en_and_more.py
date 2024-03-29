# Generated by Django 4.1.5 on 2023-01-18 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_profession_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionanswer',
            name='answer_en',
            field=models.TextField(default='sa', verbose_name='answer english'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='question_en',
            field=models.CharField(default='a', max_length=150, verbose_name='question english'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='startproject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 18, 8, 22, 0, 998117, tzinfo=datetime.timezone.utc), verbose_name='created'),
        ),
    ]
