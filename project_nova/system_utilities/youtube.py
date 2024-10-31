# import playsound as ps
import os
import yt_dlp
import subprocess
from ..speech_utilities.deliver_speech_tts import speak
from ..config import load_config


config = load_config()
Name = config["name"]

tmp_songfile_path = os.path.join(os.path.expanduser('~'), Name, "tmp", "song.wav")

def play_youtube_music(url):
    if os.path.exists(tmp_songfile_path):
        os.remove(tmp_songfile_path)
    else:
        print("Existing file does not exist") 
        
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': tmp_songfile_path, 'verbose':False,}) as video:
        info_dict = video.extract_info(f"ytsearch:{url} song", download = True)
        video_title = info_dict['title']
        
        print(video_title)
        speak(f"Playing {video_title}")
        print("Successfully Downloaded - see local folder tmp/")
        print(tmp_songfile_path)

        subprocess.Popen(["cvlc", "--intf", "dummy", "--no-video", "--quiet", "--file-caching=1000", tmp_songfile_path])

