##Sirve para descargar el audio o vídeo de un vídeo de youtube, para ejecutar hay que ubicarse en el directorio donde está e py,
##y escribir en la terminal python yaudio_downloader.py "url"

##Implementar class para proyecto

import sys
import youtube_dl

def validate_format(format_str):
    if format_str in ['1', '2']:
        return format_str
    else:
        print("Invalid format. Please provide '1' for .mp3 or '2' for .mp4.")
        sys.exit()

# Check if the correct number of command-line arguments is provided
if len(sys.argv) == 6:  # Including start and end times
    video_url = sys.argv[1]
    result_name = sys.argv[2]
    file_format = validate_format(sys.argv[3])
    start_time = sys.argv[4]
    end_time = sys.argv[5]
else:
    # Print usage instructions and exit the script
    print("Usage: python yt-download.py video_url result_name format start_time end_time")
    print("       (1 for .mp3, 2 for .mp4)")
    sys.exit()

def download_ytvid(file_ext):
    ydl_opts = {
        'format': 'bestaudio/best' if file_ext == 'mp3' else 'best',
        'keepvideo': False,
        'outtmpl': f"{result_name}.{file_ext}",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if file_ext == 'mp3' else [],
        'start_time': start_time,
        'end_time': end_time,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
        except youtube_dl.DownloadError as e:
            print("Error during download:", e)
            sys.exit()

    print(f"Download complete... {result_name}.{file_ext}")

# Call the function to download the video
download_ytvid(file_format)