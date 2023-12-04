
from PIL import Image, ImageDraw, ImageOps
import os
from django.conf import settings


# Abra as imagens

from PIL import Image
import numpy as np
import cv2
from landpage.face import face
# abrir as imagens

from PIL import Image, ImageDraw, ImageOps

def imgcirculo(image):
    imagem_maior = Image.open(os.path.join(settings.MEDIA_ROOT,'Rui.png'))

    imagem_menor = image
    # cria uma nova imagem
    nova_imagem = Image.new('RGBA', imagem_maior.size, (255, 255, 255, 0))

    # cria uma máscara redonda
    mascara = Image.new('1', imagem_maior.size, 0)
    desenho_mascara = ImageDraw.Draw(mascara)
    centro = (imagem_maior.width // 2, imagem_maior.height // 2)
    raio = imagem_maior.width // 2
    desenho_mascara.ellipse((centro[0]-raio, centro[1]-raio, centro[0]+raio, centro[1]+raio), fill=1)

    # aplica a máscara na imagem menor
    imagem_menor = ImageOps.fit(imagem_menor, mascara.size, centering=(0.5, 0.5))
    imagem_menor.putalpha(mascara)

    # cola a imagem menor na imagem maior
    nova_imagem.paste(imagem_menor, (centro[0]-imagem_menor.width//2, centro[1]-imagem_menor.height//2), imagem_menor)

    # salva a nova imagem
    nova_imagem=np.array(nova_imagem)
    nova_imagem=cv2.cvtColor(nova_imagem, cv2.COLOR_RGB2BGR)

    return nova_imagem


