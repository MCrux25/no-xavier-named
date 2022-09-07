import sys, youtube_dl
if len(sys.argv) == 2:
    
    video_url = sys.argv[1]

    def download_ytvid_as_mp3():
        
        video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        print("Download complete... {}".format(filename))
    
    download_ytvid_as_mp3()
else:
    print ("Introduce una url.")