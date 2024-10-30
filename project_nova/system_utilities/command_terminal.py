import subprocess
from .youtube import play_youtube_music
import datetime
from ..speech_utilities.deliver_speech_tts import speak

def issue_commands(commands:list):


    for command in commands:

        if "play" in command.lower()[0:5]:
            speak("Searching for the song")
            play_youtube_music(command[6:])

        else:
    
            result = subprocess.run(command.split(), capture_output=True, text=True)

            # Print the output of the command
            print("Output:")
            print(result.stdout)

            with open("./project_nova/logs/log.txt", "a") as logs:
                logs.write(f"\n\n{datetime.datetime.now()}\nCommand: {command}")

            # Print any errors if they occurred
            if result.stderr:
                print("Error:")
                print(result.stderr)
