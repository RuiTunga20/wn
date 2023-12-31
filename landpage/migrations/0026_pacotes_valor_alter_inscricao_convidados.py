# Generated by Django 4.2.4 on 2023-10-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0025_pacotes_alter_inscricao_convidados_encontrosb2b_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacotes',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='Convidados',
            field=models.CharField(choices=[('Delegado', 'Delegado'), ('Visitante ', 'Visita a área de Exposição')], default='Delegado', max_length=20),
        ),
    ]
