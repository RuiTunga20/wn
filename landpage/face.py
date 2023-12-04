import cv2
import numpy as np
from PIL import Image

def face(imagen):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    return  img
