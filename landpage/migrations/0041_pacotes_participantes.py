# Generated by Django 4.2.4 on 2023-10-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0040_alter_pacotes_patrocinio_valor_inscricao_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacotes',
            name='participantes',
            field=models.IntegerField(default=0),
        ),
    ]
