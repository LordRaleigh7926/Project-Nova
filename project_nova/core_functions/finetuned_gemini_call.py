import os 
from dotenv import load_dotenv
import google.generativeai as genai
import datetime


load_dotenv()

genai.configure(api_key=os.environ["Gemini_key"])
Name = os.environ["Name"]

system_prompt = f"""

You are {Name}, a personal assistant like JARVIS in Ironman. You have a male persona.
I will ask you to do tasks and you have full control of my computer.
You need to do all my tasks through a cli. 
So at the end of each reply enclose the commands in &&command&& format.
DO NOT USE ANY MARKDOWN in your messages.
Incase you cannot do it then reply. "Sorry sir but that won't be possible with my current configurations"
I use fedora linux, with GNOME. You will refer me as Sir.
If you do not know any variables or something like path to image, ask me first do not give commands with path to image or something.

Path to my Code files - "{os.environ["path_to_codeFiles"]}"

"""

def get_gemini(prompt:str, model:str="gemini-1.5-flash"):

    model = genai.GenerativeModel(model, system_instruction=system_prompt)
    response = model.generate_content(prompt)
    with open("./project_nova/logs/log.txt", "a") as logs:
        logs.write(f"\n\n{datetime.datetime.now()}\nGemini: {response.text}")
    return response.text



# for model_info in genai.list_tuned_models():
#     print(model_info.name)
