# Generated by Django 4.2.4 on 2023-10-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0035_pacotespatrocinio_cedulas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pacotespatrocinio',
            name='Cedula',
        ),
        migrations.AlterField(
            model_name='pacotespatrocinio',
            name='Cedulas',
            field=models.DecimalField(decimal_places=6, max_digits=7),
        ),
    ]
