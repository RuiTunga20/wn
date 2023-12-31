# Generated by Django 4.2.4 on 2023-10-18 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landpage', '0023_remove_inscricao_evento_remove_inscricao_sr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscricao',
            name='exposicao',
        ),
        migrations.RemoveField(
            model_name='inscricao',
            name='workshop',
        ),
        migrations.AddField(
            model_name='inscricao',
            name='user_updadte',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='Convidados',
            field=models.CharField(choices=[('Delegado', 'Delegado')], default='Delegado', max_length=20),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default='Masculino', max_length=20, verbose_name='Genero'),
        ),
    ]
