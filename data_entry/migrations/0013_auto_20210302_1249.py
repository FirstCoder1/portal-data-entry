# Generated by Django 3.1.7 on 2021-03-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0012_auto_20210219_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]