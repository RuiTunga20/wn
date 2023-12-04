from django.conf import settings
from django.db import models
from landpage.utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile

import cv2
import qrcode
import numpy
import os
import imutils



# Create your models here.


class prelector(models.Model):
    nome=models.CharField(max_length=200, blank=False)
    Descricao=models.CharField(max_length=200, blank=False)
    Descricao=models.CharField(max_length=200, blank=False)

    foto=models.ImageField(upload_to="media/foto")
    def __str__(self):
        return self.nome+" - "+ self.Descricao


class moderador(models.Model):
    nome=models.CharField(max_length=200, blank=False)
    Descricao=models.CharField(max_length=200, blank=False)
    foto=models.ImageField(upload_to="media/foto")

    def __str__(self):
        return self.nome +" - "+ self.Descricao
    


class Programa1(models.Model):
    Titulo=models.CharField(max_length=200, blank=False)
    prelector=models.CharField(max_length=200, blank=True,null=True)
    Tempo=models.CharField(max_length=200,  blank=True,null=True)
    horario=models.CharField(max_length=200, blank=True,null=True)
    Descricao=models.CharField(max_length=200, blank=True,null=True)
    Titulo_break = models.CharField(max_length=50, choices=[('Sim', 'Sim'), ('Não', 'Não')],default="Não")
    Ppt=models.FileField(upload_to="media/ptt", blank=True,null=True)

    def __str__(self):
        return self.Titulo

class Programa2(models.Model):
    Titulo=models.CharField(max_length=200, blank=False)
    prelector=models.CharField(max_length=200, blank=True,null=True)
    Tempo=models.CharField(max_length=200,  blank=True,null=True)
    horario=models.CharField(max_length=200, blank=True,null=True)
    Descricao=models.CharField(max_length=200, blank=True,null=True)
    Titulo_break = models.CharField(max_length=50, choices=[('Sim', 'Sim'), ('Não', 'Não')],default="Não")
    Ppt=models.FileField(upload_to="media/ptt", blank=True,null=True)

    def __str__(self):
        return self.Titulo


class NOTICIA(models.Model):
    Titulo=models.CharField(max_length=200, blank=False)
    Descricao=models.CharField(max_length=200, blank=True,null=True)
    fotos=models.FileField(upload_to="media/noticia", blank=True,null=True)
    data=models.DateField()


    def __str__(self):
        return self.Titulo

from django.db import models
from django.utils import timezone

class Inscricao(models.Model):
    ESTADO_CHOICES = (
        ('Aguardando', 'Aguardando'),
        ('Rejeitado', 'Rejeitado'),
        ('Aceite', 'Aceite'),
    )
    Convidados = (
        ('Delegado', 'Delegado'),
        ('Visitante ', 'Visita a área de Exposição'),
       

    )
   

    Genero = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),

    )

    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    empresa = models.CharField('Nome da Instituição',max_length=100)
    urt= models.CharField('Website',max_length=100,blank=True,null=True)
    Pais = models.CharField('País de Origem ',max_length=100)
    email = models.EmailField(unique=True)
    genero = models.CharField('Genero',max_length=20, choices=Genero, default='Masculino')

    telefone = models.CharField(max_length=20)
    Convidados= models.CharField(max_length=20, choices=Convidados, default='Delegado')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Aguardando')
    
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images',null=True,blank=True,default='Vazio')
    user_updadte= models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        default=1
    )


    def __str__(self):
        return self.nome
   

   
        self.godigoqr()  # Gera o código QR
        super().save(*args, **kwargs)

        # Abre o código QR gerado
        qr_image = Image.open(os.path.join(settings.MEDIA_ROOT, f'qrcode_{self.nome}.png'))

        # Abre a imagem associada a esta instância
        pil_img = Image.open(os.path.join(settings.MEDIA_ROOT, 'RUI.png'))

        # Redimensiona o código QR
        nova_largura = 300
        nova_altura = 300
        imagem_redimensionada = qr_image.resize((nova_largura, nova_altura))

        # Sobreponha o código QR redimensionado à imagem
        pil_img.paste(imagem_redimensionada, (450, 700), imagem_redimensionada)

        # Salva a imagem final processada com um nome específico na pasta de mídia
        nome_imagem_final = f'Tomas_qrcode_{self.nome}.png'
        caminho_imagem_final = os.path.join(settings.MEDIA_ROOT, nome_imagem_final)
        pil_img.save(caminho_imagem_final)

        # Atualiza o campo da instância com o nome da imagem final processada

class Pacotes(models.Model):
       nome = models.CharField(max_length=100)
       valor=models.DecimalField(max_digits=10,decimal_places=2)
       participantes=models.IntegerField(default=0)
       def __str__(self):
           return self.nome
class PacotesPatrocinio(models.Model):
       nome = models.CharField(max_length=100)
       valor=models.DecimalField(max_digits=10,decimal_places=2)


       def __str__(self):
           return self.nome

class Pacotes_Patrocinio(models.Model):
       nome = models.CharField(max_length=100)
       valor=models.DecimalField(max_digits=10,decimal_places=6)


       def __str__(self):
           return self.nome


class Empresa(models.Model):
    ESTADO_CHOICES = (
        ('Aguardando', 'Aguardando'),
        ('Rejeitado', 'Rejeitado'),
        ('Aceite', 'Aceite'),
    )
   
    nome = models.CharField(max_length=100)
    site= models.CharField('Website',max_length=100,blank=True,null=True)
    Pais = models.CharField('País de Origem ',max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    Pacotes= models.ForeignKey(Pacotes, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Aguardando')
    
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images',null=True,blank=True,default='Vazio')
    user_updadte= models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        default=1
    )
    def __str__(self):
           return self.nome


class encontrosb2b(models.Model):
    ESTADO_CHOICES = (
        ('Aguardando', 'Aguardando'),
        ('Rejeitado', 'Rejeitado'),
        ('Aceite', 'Aceite'),
    )
   
    nome = models.CharField(max_length=100)
    site= models.CharField('Website',max_length=100,blank=True,null=True)
    Pais = models.CharField('País de Origem ',max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Aguardando')
    
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images',null=True,blank=True,default='Vazio')
    user_updadte= models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        default=1
    )
    def __str__(self):
           return self.nome
    

class EmpresaPatrocinio(models.Model):
    ESTADO_CHOICES = (
        ('Aguardando', 'Aguardando'),
        ('Rejeitado', 'Rejeitado'),
        ('Aceite', 'Aceite'),
    )
   
    nome = models.CharField(max_length=100)
    site= models.CharField('Website',max_length=100,blank=True,null=True)
    Pais = models.CharField('País de Origem ',max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    Pacotes= models.ForeignKey(Pacotes_Patrocinio, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Aguardando')
    
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images',null=True,blank=True,default='Vazio')
    user_updadte= models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        default=1
    )
    def __str__(self):
           return self.nome


class Inscricao_empresa(models.Model):
    

    Genero = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),

    )

    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    genero = models.CharField('Genero',max_length=20, choices=Genero, default='Masculino')
    telefone = models.CharField(max_length=20)
    Pais = models.CharField('País de Origem ',max_length=100)
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images',null=True,blank=True,default='Vazio')
    user_updadte= models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        default=1
    )


    def __str__(self):
        return self.nome