import ollama
import datetime

def process_command_with_ollama(command):
    try:
        response = ollama.chat(model='llama2-uncensored:latest', messages=[
            {
                'role': 'user',
                'content': command,
            },
        ])

        with open("./project_nova/logs/log.txt", "a") as logs:
            logs.write(f"\n\n{datetime.datetime.now()}\nLlama: {response.text}")

        return response['message']['content']
    
    except Exception as e:
        print(f"Error processing command with Ollama: {e}")

        with open("./project_nova/logs/errors.txt", "a") as errors:
            errors.write(f"\n\n{datetime.datetime.now()}\nLlama_error: {e}")

        return None