import subprocess
import re
from gale import solve_err 

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

def execute_cmd(cmds):
    err_occured = False
    for command in cmds:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        print(f'Command : {command}')
        # auto_indentation = ["autopep8 my_script.py --in-place"]
        # result = subprocess.run(auto_indentation, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.returncode != 0:
            print("Command failed with error message:")
            print(result.stderr)
            err = result.stderr
            err_occured = True
            break;
        print(result.stdout);
    if(err_occured):
        solve_err(err)

if __name__ == "__main__":
    content = input("Test Input")
    process_file_and_write(content)