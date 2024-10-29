# Speech utility functions
from .speech_utilities.capture_speech import takeCommand
from .speech_utilities.deliver_speech_tts import speak, alt_speak


# Main AI, models imports
from .core_functions.finetuned_gemini_call import get_gemini
from .core_functions.llama_call import process_command_with_ollama

# System Utilites
from .system_utilities.command_terminal import issue_commands

# Other functions
from .other_functions import internet_status, preprocess_response_gemini


# General
import os 
from dotenv import load_dotenv


load_dotenv()

Name = str(os.environ["Name"])

internet_access = internet_status()
nova_listening = False

speak(f"{Name} Online")

while True:
        
        query = takeCommand(internet_status).lower()

        if not query == "":

            if "cancel" in query:
                continue

            if Name.lower() in query:
                print("-"*100)
                nova_listening = True

            if ("peace out" or "peaceout") in query:
                print("---")
                nova_listening = False

            if nova_listening:

                if internet_access:
                    response = get_gemini(query)
                    response, commands = preprocess_response_gemini(response)
                    issue_commands(commands)

                else:
                    response = process_command_with_ollama(query)

                speak(response)

        print("nova_listening:", nova_listening)

