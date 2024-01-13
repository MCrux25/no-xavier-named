import os
from PIL import Image, ImageFilter, ImageEnhance
from pathlib import Path
from tqdm import tqdm
import random

rand = random.randint(0,5)

print (rand)

##sirve para definir directorio base
BASE_DIR = Path(__file__).resolve().parent.parent

##Directorio de imagenes a reescalar
source_path = '{BASE_DIR}/source'
if not os.path.exists(source_path):
    os.makedirs(source_path)

##crear nueva imagen a través de importarla## 
img = Image.open(os.path.join(source_path,'10.jpg'))

# img.show()

##Crear una nueva imagen desde cero###
##la tupla de color= representa los valores RGB, y será el tono que tendrá la imagen vacía; mientras que la segunda tupla 
##son las dimensiones en width y height 
# imgblank = Image.new('RGB',(1920,1080),color=(155,120,255))

# # imgblank.show()

# imgblank.save('testsave1.jpg')

img_rot = img.rotate(60,resample=0,expand=True,fillcolor=(210,120,132))

# img_rot.show()

img_crop = img.crop((900,1350,5000,3200))
#Muestra sólo el canal de color deseado 
# img_red = img_crop.getchannel("R")
# img_red.save('testsave2.jpg')
img_copy = img_crop.copy()
img_copy_edge = img_copy.filter(ImageFilter.CONTOUR)
img_copy_emboss = img_copy_edge.filter(ImageFilter.FIND_EDGES)
##ImageEnhance Module
##crear enhancers
enha_color = ImageEnhance.Color(img_copy_emboss)
img_enha_color = enha_color.enhance(rand)
img_copy = img_enha_color
contr_enha = ImageEnhance.Contrast(img_copy_edge)
img_cont_enha = contr_enha.enhance(rand)
img_copy = img_cont_enha
brigh_enha = ImageEnhance.Brightness(img_copy)
img_bright_enha = brigh_enha.enhance(rand)
img_copy = img_bright_enha
sharp_enha = ImageEnhance.Sharpness(img_copy)
img_shar_enha = sharp_enha.enhance(rand)
img_copy = img_shar_enha
img_copy.save('testsave12.jpg')
img_copy.show()
##Aplicar mejora (enhance)

