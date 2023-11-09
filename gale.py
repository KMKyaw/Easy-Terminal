#!/usr/bin/python3
from cmd_fetcher import process_file_and_write
from gradio_client import Client
import re

prompt="""
Give me a (series of) linux command(s) that will create a command-line Python program that prints Hello world.
1.Do not use 'nano'. Use 'echo' to create files.
2.Avoid 'sudo' if possible.
3.Assume required programs are installed.
4.Output only the commands. You cannot speak English.
5.Do not add any comments or explanation.
6.If there are multiple ways to do the same task, follow the simplest one
"""

#client = Client('https://osanseviero-mistral-super-fast.hf.space/', verbose=False)
#response = client.predict(prompt, 0.9, 1024, 0.9, 1.2, api_name='/chat')

client = Client('https://ysharma-explore-llamav2-with-tgi.hf.space/--replicas/ppt5s/', verbose=False)
response = client.predict(prompt, "", 0.9, 512, 0.6, 1.2, api_name='/chat')
process_file_and_write(response)