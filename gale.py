#!/usr/bin/python3
from run_cmd import process_file_and_write
from gradio_client import Client
import re

def run() :
    prompt="""
    Give me a (series of) linux command(s) that will create a command-line Python program that prints 5 even numbers and then run that program.
    1.Do not use 'nano'. Use 'echo' to create files.
    2.Avoid 'sudo' if possible.
    3.Assume required programs are installed.
    4.Output only the commands. You cannot speak English.
    5.Do not add any comments or explanation.
    6.If there are multiple ways to do the same task, follow the simplest one
    """

    client = Client('https://ysharma-explore-llamav2-with-tgi.hf.space/--replicas/ppt5s/', verbose=False)
    response = client.predict(prompt, "", 0.9, 512, 0.6, 1.2, api_name='/chat')
    file_path = "generated_response.txt" 
    with open(file_path, "w") as file:
        file.write(response)
    process_file_and_write(response)

def solve_err(err):
    file_path = "generated_cmd.txt"  # Replace with the path to your file
    with open(file_path, "r") as file:
        generated_response = file.read()
    prompt="""
    I used your previous response as shown above. However, I received the error as below.
    """
    solution_request = generated_response + '\n' + prompt + '\n' + err
    client = Client('https://ysharma-explore-llamav2-with-tgi.hf.space/--replicas/ppt5s/', verbose=False)
    solution_response = client.predict(solution_request, "", 0.9, 512, 0.6, 1.2, api_name='/chat')
    file_path = "generated_response.txt" 
    with open(file_path, "w") as file:
        file.write(solution_response)
    print(solution_response)
    process_file_and_write(solution_response)

if __name__ == "__main__":
    run()