##Sirve para descargar el audio de un vídeo de youtube, para ejecutar hay que ubicarse en el directorio donde está e py,
##y escribir en la terminal python yaudio_downloader.py "url"

##Implementar class para proyecto

import sys, youtube_dl

if len(sys.argv) == 2:
    
    # video_url = sys.argv[1]

    # def download_ytvid_as_mp3():
        
    #     video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    #     filename = f"{video_info['title']}.mp3"
    #     options={
    #         'format':'bestaudio/best',
    #         'keepvideo':False,
    #         'outtmpl':filename,
    #     }
    #     with youtube_dl.YoutubeDL(options) as ydl:
    #         ydl.download([video_info['webpage_url']])
    #     print("Download complete... {}".format(filename))
    
    # download_ytvid_as_mp3()

    video_url = sys.argv[1]

    def download_ytvid_as_mp4():
        
        video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
        filename = f"{video_info['title']}.mp4"
        options={
            'format':'best',
            'keepvideo':False,
            'outtmpl':filename,
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        print("Download complete... {}".format(filename))
    
    download_ytvid_as_mp4()
else:
    print ("Introduce una url.")