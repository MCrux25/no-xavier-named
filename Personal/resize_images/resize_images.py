import os
from PIL import Image
from pathlib import Path
from tqdm import tqdm


##sirve para definir directorio base
BASE_DIR = Path(__file__).resolve().parent.parent

##Directorio de imagenes a reescalar
source_path = '{BASE_DIR}/source'
if not os.path.exists(source_path):
    os.makedirs(source_path)

##directorio de imagenes reescaladas
desth_path = '{BASE_DIR}/img_rescaladas'
if not os.path.exists(desth_path):
    os.makedirs(desth_path)

# Tamaño deseado de las imágenes
nuevo_ancho = int(input('¿Cual será el nuevo ancho de las imágenes? *Medida en pixeles'))
nuevo_alto = int(input('¿Cual será el nuevo alto de las imágenes? *Medida en pixeles'))

def resize():
    for filename in tqdm(os.listdir(source_path)):
    # Comprobamos que el archivo sea una imagen en formato JPEG
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            # Abrimos la imagen
            imagen = Image.open(os.path.join(source_path, filename))
            # Redimensionamos la imagen
            imagen = imagen.resize((nuevo_ancho, nuevo_alto))
            # Guardamos la nueva imagen en la carpeta de destino
            imagen.save(os.path.join(desth_path, filename))

    print ("Se han reescalado todas las imágenes")

def delete_originals():
    for filename in tqdm(os.listdir(source_path)):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            os.remove(os.path.join(source_path, filename))

    print ("Se han eliminado las imágenes originales")

resize ()
delete_originals()