import requests
import os
import google.generativeai as genai
import time
import pandas as pd
import seaborn as sns


# THIS IS NOT A PART OF MAIN PROJECT NOVA















genai.configure(api_key=os.environ['Gemini_key'])
Name = os.environ["Name"]

base_model = "models/gemini-1.5-flash-001-tuning"
training_data = [
    {"text_input": "open vscode", "output": "Sure sir. &&code&&"},
    {"text_input": "Nova can you please open the browser?", "output": "&&microsoft-edge-stable&&"},
    {"text_input": "Nova, can you list the files in this directory?", "output": "Certainly! &&ls&&"},
    {"text_input": "Hey Nova, open the terminal", "output": "Sure thing! &&gnome-terminal&&"},
    {"text_input": "Nova, shut down the system", "output": "Shutting down. &&shutdown now&&"},
    {"text_input": "Can you check the current directory?", "output": "Here you go: &&pwd&&"},
    {"text_input": "Nova, update my system", "output": "I'll update the system for you. &&sudo dnf update -y&&"},
    {"text_input": "Create a new directory called 'Projects'", "output": "Creating directory 'Projects'. &&mkdir Projects&&"},
    {"text_input": "Nova, remove the 'test' folder", "output": "Deleting 'test' folder. &&rm -r test&&"},
    {"text_input": "Nova, what's my disk usage?", "output": "Here's the disk usage. &&df -h&&"},
    {"text_input": "Open settings", "output": "Opening settings. &&gnome-control-center&&"},
    {"text_input": "Nova, show the running processes", "output": "Here are the running processes. &&ps aux&&"},
    {"text_input": "Nova, kill process with PID 1234", "output": "Terminating process with PID 1234. &&kill 1234&&"},
    {"text_input": "Switch to workspace 2", "output": "Switching to workspace 2. &&wmctrl -s 1&&"},
    {"text_input": "Nova, lock the screen", "output": "Locking the screen. &&gnome-screensaver-command -l&&"},
    {"text_input": "Nova, who invented the computer?", "output": "The concept of a programmable computer was first proposed by Charles Babbage, often called the 'father of the computer.'"},
    {"text_input": "Can you tell me the capital of France?", "output": "The capital of France is Paris."},
    {"text_input": "Nova, what's 25 times 4?", "output": "The answer is 100."},
    {"text_input": "Nova, who developed Linux?", "output": "Linux was originally developed by Linus Torvalds in 1991."},
    {"text_input": "What's the largest planet in our solar system?", "output": "The largest planet in our solar system is Jupiter."},
    {"text_input": "Nova, can you tell me a joke?", "output": "Why do programmers prefer dark mode? Because light attracts bugs!"},
    {"text_input": "Nova, what's the speed of light?", "output": "The speed of light is approximately 299,792 kilometers per second, or about 186,282 miles per second."},
    {"text_input": "What is the distance to the moon?", "output": "The average distance to the moon is about 384,400 kilometers (238,855 miles)."},
    {"text_input": "Nova, who is the CEO of Google?", "output": "The CEO of Google is Sundar Pichai."},
    {"text_input": "Nova, what's the square root of 144?", "output": "The square root of 144 is 12."},
    {"text_input": "Nova, give me a random fact", "output": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!"}

]

operation = genai.create_tuned_model(
    # You can use a tuned model here too. Set `source_model="tunedModels/..."`
    display_name="increment",
    source_model=base_model,
    epoch_count=40,
    batch_size=4,
    learning_rate=0.001,
    training_data=training_data,
)

for status in operation.wait_bar():
    time.sleep(10)

result = operation.result()
print(result)
# # You can plot the loss curve with:
snapshots = pd.DataFrame(result.tuning_task.snapshots)
sns.lineplot(data=snapshots, x='epoch', y='mean_loss')

model = genai.GenerativeModel(model_name=result.name)
result = model.generate_content("III")
print(result.text)  # IV