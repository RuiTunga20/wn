# Generated by Django 4.2.4 on 2023-10-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0030_pacotespatrocinio_empresapatrocinio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacotespatrocinio',
            name='valor',
            field=models.DecimalField(decimal_places=9, max_digits=9),
        ),
    ]
