# Generated by Django 3.1.4 on 2021-02-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0010_auto_20210219_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]