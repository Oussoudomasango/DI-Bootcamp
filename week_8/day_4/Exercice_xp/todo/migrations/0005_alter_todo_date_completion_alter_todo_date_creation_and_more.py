# Generated by Django 4.1.3 on 2022-12-01 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_date_completion_alter_todo_date_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_completion',
            field=models.DateTimeField(default=datetime.date(2022, 12, 1)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 13, 11, 59, 847795)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_echeance',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 13, 11, 59, 847829)),
        ),
    ]
