from gradio_client import Client
from run_cmd import execute_cmd
import re

def process_file_and_write(content):
    matches = re.findall(r"```(.*?)```", content, re.DOTALL)

    if matches:
        clean_response = matches[0].strip()  # Get the first match and remove leading/trailing whitespace
    else:
        clean_response = "No content between triple backticks found."

    # Split the input_string into an array of lines
    cmds = clean_response.split('\n')
    file_path = "generated_cmd.txt" 
    with open(file_path, "w") as file:
        file.write(clean_response)
    execute_cmd(cmds)

if __name__ == "__main__":
    content = input("Test Input")
    process_file_and_write(content)