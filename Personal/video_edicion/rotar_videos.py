import os
import sys
from tqdm import tqdm
from moviepy.editor import VideoFileClip
from pathlib import Path

##sirve para abrir desde terminal, usando python rotar_videos.py [grados de rotación de vídeos]
if len(sys.argv) == 2:
    rotacion = int(sys.argv[1])
else:
    print("Por favor, proporciona el ángulo de rotación como argumento.")
    sys.exit()

##sirve para definir directorio base
BASE_DIR = Path(__file__).resolve().parent.parent

##Directorio de videos a reescalar
source_path = '{BASE_DIR}/source'
if not os.path.exists(source_path):
    os.makedirs(source_path)

##directorio de videos reescalados
dest_path = '{BASE_DIR}/videos_rotados'
if not os.path.exists(dest_path):
    os.makedirs(dest_path)

def rotar_videos():
    for filename in tqdm(os.listdir(source_path)):
        if filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.mkv'):
            # Ruta completa del archivo de origen
            source_file = os.path.join(source_path, filename)
            
            # Ruta completa del archivo de destino
            dest_file = os.path.join(dest_path, filename)
            
            # Abrimos el video 
            
            video = VideoFileClip(source_file)

            # Rotamos el video
            video = video.rotate(rotacion)
            
            # Guardamos el nuevo video en la carpeta de destino
            video.write_videofile(dest_file)
    
    print("Se han girado todos los vídeos")

rotar_videos()