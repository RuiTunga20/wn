
from PIL import Image
from rembg import remove
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
from PIL import Image, ImageDraw, ImageOps
import cv2
import imutils
from landpage.imgcirculo import imgcirculo as circulo
from landpage.face import face as caras

from django.core.files.base import ContentFile
import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse

def face(imagen):

    img =  imagen

    

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt.xml')
    face_eyes = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_lefteye_2splits.xml')
    eyes = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=2, minSize=(30, 30))
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6, minSize=(30, 30))

    for (x, y, w, h) in faces:
        if len(eyes) == 1:
            for (x1, y1, w1, h1) in eyes:
                img=img[(y-100):(y + h+150), (x-100):(x + w+150)]

        else:
            eyes = face_eyes.detectMultiScale(gray, scaleFactor=1.9, minNeighbors=2, minSize=(30, 30))
            if len(eyes) == 1:
                for (x1, y1, w1, h1) in eyes:

                    img=img[(y-100):(y + h+150), (x-100):(x + w+150)]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    return  img


def imgcirculo(image):

# Crie uma nova imagem de fundo
    background = Image.new("RGBA", image.size, (0, 0, 0, 0))


    # Crie uma máscara de círculo
    mask = Image.new("L", image.size, 1)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((1, 0) + image.size, fill=500)

    # Cole a imagem original na nova imagem de fundo usando a máscara de círculo
    background.paste(image, (0, 0), mask)
    # salva a nova imagem


    nova_imagem=np.array(background)
    nova_imagem=cv2.cvtColor(nova_imagem, cv2.COLOR_RGB2BGR)

    return nova_imagem


# Front Image
def get_filtered_image(image, action):
    fnt = ImageFont.truetype(os.path.join(settings.MEDIA_ROOT, "Montserrat-SemiBold.ttf"), 35)
    filename = caras(image)
    filename=circulo(filename)

    # Back Image0
    filename1 = os.path.join(settings.MEDIA_ROOT, 'Rui.png')
    background = Image.open(filename1)
    novo=filename
    texto = action
    #novo[...,[0,2]]=novo[...,[2,0]]
    draw = ImageDraw.Draw(background)
    draw.text((125, 298), texto, (13, 161, 32),fnt)

    try:
        rt=imutils.resize(novo,width=400)
        rt=Image.fromarray(rt)
    except Exception as e:
        print(e)
    rt=rt.convert("RGBA")
    background = background.convert("RGBA")
    background.paste(rt, (480,400), rt)
    return background


