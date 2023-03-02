from moviepy.editor import*
import sys

if len(sys.argv) == 5:
    
    filename = sys.argv[1]
    result_name = sys.argv[2]
    t0 = int(sys.argv[3])
    t1 = int(sys.argv[4])

    def cut_video():

    ##recortar video (t0=segundo inicial, t1=segundo final)
        video = VideoFileClip(f'{filename}')  ##abrir vídeo, especificar ruta
        cortado = video.subclip(t0, t1)
        cortado.write_videofile(f'{result_name}.mp4')
        print("kotin complit... {}".format(result_name))
    
    cut_video()
else:
    print ('Introduce la información así: python editar_videos.py filename/filename route result_name t0 t1')