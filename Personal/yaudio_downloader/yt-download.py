##Sirve para descargar el audio o vídeo de un vídeo de youtube, para ejecutar hay que ubicarse en el directorio donde está e py,
##y escribir en la terminal python yaudio_downloader.py "url"

##Implementar class para proyecto

import sys
import youtube_dl

if len(sys.argv) == 3:
    video_url = sys.argv[1]
    result_name = sys.argv[2]
    # file_format = sys.argv[3]
else:
    print("Introduce la información así: python yt-download.py route result_name format (1 for .mp3, 2 for .mp4)")
    sys.exit()

# def download_ytvid_as_mp3():
#     video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
#     filename = f"{result_name}.mp3"

#     # Definir el tiempo de inicio y fin del fragmento deseado
#     start_time = "00:00:00"  # Ejemplo: 30 segundos
#     end_time = "00:03:38"  # Ejemplo: 1 minuto y 30 segundos

#     options = {
#         'format': 'bestaudio/best',
#         'keepvideo': False,
#         'outtmpl': filename,
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#         'start_time': start_time,
#         'end_time': end_time
#     }

#     with youtube_dl.YoutubeDL(options) as ydl:
#         ydl.download([video_info['webpage_url']])

#     print("Download complete... {}".format(filename))

def download_ytvid_as_mp4():
    video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=True)
    filename = f"{result_name}.mp4"
    options = {
        'format': 'best',
        'keepvideo': False,
        'outtmpl': filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))

download_ytvid_as_mp4()

# if file_format == '1':
#     download_ytvid_as_mp3()
# elif file_format == '2':
#     download_ytvid_as_mp4()
# else:
#     print("Invalid format. Please provide '1' for .mp3 or '2' for .mp4.")