# Generated by Django 4.2.4 on 2023-08-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0010_alter_noticia_fotos_alter_programa1_ppt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('estado', models.CharField(choices=[('Aguardando', 'Aguardando'), ('Rejeitado', 'Rejeitado'), ('Aceite', 'Aceite')], default='Aguardando', max_length=20)),
            ],
        ),
    ]
