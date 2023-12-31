# Generated by Django 4.2.4 on 2023-10-18 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0038_alter_pacotespatrocinio_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pacotes_Patrocinio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='empresapatrocinio',
            name='Pacotes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landpage.pacotes_patrocinio'),
        ),
    ]
