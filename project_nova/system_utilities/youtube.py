import os
import yt_dlp as youtube_dl
import subprocess

def play_youtube_music(song_name):
    # Define the path where the song will be saved
    tmp_songfile_path = os.path.join(os.path.expanduser('~'), "Nova", "tmp", "csong.mp3")
    
    # Remove the existing file if it exists
    if os.path.exists(tmp_songfile_path):
        os.remove(tmp_songfile_path)
    
    ydl_opts = {
        'format': 'bestaudio',  # Use 'bestaudio' directly
        'quiet': True,
        'outtmpl': tmp_songfile_path,  # Save to the specified path
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # You can try '320' for better quality
        }],
    }
    
    # Search and download the audio
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{song_name}", download=True)['entries'][0]
        print(f"Downloaded song: {info['title']}")

    # Play the downloaded audio
    subprocess.Popen(["cvlc", "--intf", "dummy", "--no-video", "--quiet", "--file-caching=1000", tmp_songfile_path])

# Example usage
play_youtube_music("unstoppable")
