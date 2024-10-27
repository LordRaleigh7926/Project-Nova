import speech_recognition as sr
import datetime


def takeCommand():
    
    r = sr.Recognizer()
    r.pause_threshold = 1.0 #Amount of time it waits for a sentence to be considered complete
    
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"\n\n{datetime.datetime.now()}\nUser said: {query}")

        with open("./project_nova/logs/log.txt", "a") as logs:
            logs.write(f"\n\n{datetime.datetime.now()}\nUser: {query}")

    except Exception as e:

        print("Unable to Recognize your voice.")  
        return ""
    
    return query