# Generated by Django 2.1.11 on 2019-12-15 18:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0009_auto_20191215_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_created_by_author',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 18, 56, 48, 9138, tzinfo=utc)),
        ),
    ]
