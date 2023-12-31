# Generated by Django 4.2.4 on 2023-10-20 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landpage', '0039_pacotes_patrocinio_alter_empresapatrocinio_pacotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacotes_patrocinio',
            name='valor',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.CreateModel(
            name='Inscricao_empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default='Masculino', max_length=20, verbose_name='Genero')),
                ('telefone', models.CharField(max_length=20)),
                ('Pais', models.CharField(max_length=100, verbose_name='País de Origem ')),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('data_updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, default='Vazio', null=True, upload_to='images')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landpage.empresa')),
                ('user_updadte', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
