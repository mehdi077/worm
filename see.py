import subprocess
import time
session_name = str(input("session name: "))
def get_tmux_output(session_name):
    try:
        return subprocess.check_output(['tmux', 'capture-pane', '-t', session_name, '-p']).decode()
    except:
        return ""

def main():
    pass
if __name__ == "__main__":
    while True:
        print(get_tmux_output(session_name))
    