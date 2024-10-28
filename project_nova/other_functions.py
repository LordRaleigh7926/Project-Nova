from urllib import request
import re

def internet_status():
    try:
        request.urlopen('http://google.com', timeout=2)
        print("Internet Present")
        return True
    except request.URLError as err:
        print("Internet Not Present")
        return False

def preprocess_response_gemini(response:str):

    commands = re.findall(r'\&\&(.*?)\&\&', response) # Also erases the &&&& signs

    # Remove all occurrences from the original string
    modified_text = re.sub(r'\&\&(.*?)\&\&', '', response).strip()
    
    return modified_text, commands
