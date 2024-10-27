import subprocess
import pyttsx3
import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume', 0.9)


# This project uses the external package flite for text to speech
def speak(ctx):

    with open("./project_nova/logs/log.txt", "a") as logs:
        logs.write(f"\n\n{datetime.datetime.now()}\nNova: {ctx}")

    subprocess.Popen(["/usr/bin/flite", "-voice", "slt", ctx])


def alt_speak(ctx):
    engine.say(ctx)
    engine.runAndWait()