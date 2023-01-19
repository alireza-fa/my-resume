# Generated by Django 4.1.5 on 2023-01-19 00:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_questionanswer_answer_en_questionanswer_question_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photogallery',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AlterField(
            model_name='startproject',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 0, 33, 53, 489016, tzinfo=datetime.timezone.utc), verbose_name='created'),
        ),
    ]
