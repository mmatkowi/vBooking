# Generated by Django 3.2.7 on 2021-09-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210915_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
