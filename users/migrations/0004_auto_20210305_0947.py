# Generated by Django 3.1.7 on 2021-03-05 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210305_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(default=None, max_length=254, unique=True),
        ),
    ]
