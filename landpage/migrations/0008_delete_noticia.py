# Generated by Django 4.1.5 on 2023-05-10 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0007_rename_imagem_noticia_fotos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Noticia',
        ),
    ]
