# Generated by Django 3.2.7 on 2021-09-15 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210915_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='entry',
            field=models.CharField(blank=True, choices=[('paid', 'Bezahlt'), ('vip', 'Gästeliste')], max_length=4),
        ),
        migrations.AddField(
            model_name='reservation',
            name='proof',
            field=models.CharField(choices=[('tested', 'Getestet'), ('vaccinated', 'Geimpft'), ('revovered', 'Genesen')], default='tested', max_length=10),
            preserve_default=False,
        ),
    ]
