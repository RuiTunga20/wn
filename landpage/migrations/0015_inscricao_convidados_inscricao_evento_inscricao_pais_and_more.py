# Generated by Django 4.2.4 on 2023-08-31 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0014_inscricao_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricao',
            name='Convidados',
            field=models.CharField(choices=[('Delegado', 'Aguardando'), ('Visitante', 'Visitante'), ('Imprensa', 'Visitante'), ('Imprensa', 'Visitante')], default='Conferencia', max_length=20),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='Evento',
            field=models.CharField(choices=[('Conferencia', 'Conferencia'), ('Whorkshop', 'Whorkshop'), ('Exposição', 'Exposição')], default='Conferencia', max_length=20),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='Pais',
            field=models.CharField(default=1, max_length=100, verbose_name='País de Origem '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscricao',
            name='urt',
            field=models.URLField(default=1, verbose_name='WebSite da Instituição'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='empresa',
            field=models.CharField(max_length=100, verbose_name='Nome da Instituição'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]