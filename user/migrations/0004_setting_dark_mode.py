# Generated by Django 2.2.10 on 2020-06-13 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200409_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='dark_mode',
            field=models.BooleanField(default=True),
        ),
    ]
