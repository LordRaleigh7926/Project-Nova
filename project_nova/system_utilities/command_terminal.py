import subprocess

def issue_commands(commands:list):


    for command in commands:
    
        result = subprocess.run(command.split(), capture_output=True, text=True)

        # Print the output of the command
        print("Output:")
        print(result.stdout)

        # Print any errors if they occurred
        if result.stderr:
            print("Error:")
            print(result.stderr)
