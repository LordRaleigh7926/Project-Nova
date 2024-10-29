import speech_recognition as sr
import datetime


def takeCommand(internet_status:bool):
    
    r = sr.Recognizer()
    r.pause_threshold = 1.0 
    r.energy_threshold = 350

    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        if internet_status:
            query = r.recognize_google(audio, language='en-in')
        else:
            query = r.recognize_sphinx(audio, language='en-in')

        print(f"\n\n{datetime.datetime.now()}\nUser said: {query}")

        with open("./project_nova/logs/log.txt", "a") as logs:
            logs.write(f"\n\n{datetime.datetime.now()}\nUser: {query}")

    except Exception as e:

        print("Unable to Recognize your voice.")
        return ""
    
    return query