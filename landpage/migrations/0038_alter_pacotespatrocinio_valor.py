# Generated by Django 4.2.4 on 2023-10-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0037_remove_pacotespatrocinio_cedulas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacotespatrocinio',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
