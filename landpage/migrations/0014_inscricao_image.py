# Generated by Django 4.2.4 on 2023-08-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0013_alter_inscricao_data_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricao',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
