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
I use fedora linux, with GNOME. You will refer me as Sir.
Do not give commands with path/to/image or something similar.
My username is lordraleigh.
I use the dark mode in GNOME so to change my wallpaper you have to use picture-uri-dark in side the command.
Path to my code files - {os.environ["path_to_codeFiles"]}
Path to my Wallpaper Folder - {os.environ["path_to_wallpapers"]}
All the pictures inside are named 1.jpg, 2.jpg, ..., 6.jpg.
"""


generation_config = {
"temperature": 1,
"top_p": 0.95,
"top_k": 64,
"max_output_tokens": 8192,
"response_mime_type": "text/plain",

}
    
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=system_prompt)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_prompt,
)
chat_session = model.start_chat(
    history=[]
)

def get_gemini(prompt:str):

    response = chat_session.send_message(prompt)
    
    with open("./project_nova/logs/log.txt", "a") as logs:
        logs.write(f"\n\n{datetime.datetime.now()}\nGemini: {response.text}")

    return response.text






# for model_info in genai.list_tuned_models():
#     print(model_info.name)
