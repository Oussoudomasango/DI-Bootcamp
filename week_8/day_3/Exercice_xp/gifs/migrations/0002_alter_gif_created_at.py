# Generated by Django 4.1.2 on 2022-10-26 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gif',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 12, 3, 11, 426326)),
        ),
    ]