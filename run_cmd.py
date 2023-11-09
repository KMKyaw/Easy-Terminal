import subprocess

def execute_cmd(cmds):
    for command in cmds:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        print(f'Command : {command}')
        if result.returncode != 0:
            print("Command failed with error message:")
            print(result.stderr)
            break;
        print(result.stdout);
if __name__ == "__main__":
    command = 'echo "hello world"'
    execute_cmd([command])
