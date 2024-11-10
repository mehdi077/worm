import subprocess
import time

def kill_existing_session():
    subprocess.run(['tmux', 'kill-session', '-t', 'llama1'], stderr=subprocess.DEVNULL)

def create_and_setup_session():
    subprocess.run(['tmux', 'new-session', '-d', '-s', 'llama1'])
    # Set larger window size (adjust height and width as needed)
    # subprocess.run(['tmux', 'resize-window', '-t', 'llama1', '-x', '200', '-y', '1000'])
    
    commands = [
        'ssh root@172.232.34.167',
        'cd llama.cpp',
        './llama-cli -m /root/models/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-Q8_0-imat.gguf -cnv -mli'
    ]
    
    for cmd in commands:
        subprocess.run(['tmux', 'send-keys', '-t', 'llama1', cmd, 'Enter'])

def get_tmux_output():
    try:
        return subprocess.check_output(['tmux', 'capture-pane', '-t', 'llama1', '-p']).decode()
    except:
        return ""

def main():
    kill_existing_session()
    create_and_setup_session()
    
    # Wait for initial prompt
    while True:
        output = get_tmux_output()
        if "To return control without starting a new line, end your input with" in output:
            time.sleep(5)
            # print(output)
            break
        time.sleep(1)
    
    
    # while True:
    #     # Wait for '>' prompt
    #     while True:
    #         current_output = get_tmux_output()
    #         if '>' in str(current_output[-2:]):
    #             break
    #         time.sleep(2)
        
    #     # Get user input and send it
    #     user_input = input(">> ")
    #     subprocess.run(['tmux', 'send-keys', '-t', 'llama1', user_input, 'Enter'])
    #     # print(get_tmux_output())
    #     time.sleep(2)
    #     while True:
    #         current_output = get_tmux_output()
    #         if '>' in str(current_output[-2:]):
    #             output = current_output.split(">")[-2].split("\n")[1:]
                
    #             print("\n".join(output)) 
                
    #             break
    #         time.sleep(2)

def chat(prmpt):

    while True:
        current_output = get_tmux_output()
        if '>' in str(current_output[-2:]):
            break
        time.sleep(2)
    
    # Get user input and send it
    user_input = str(prmpt)
    subprocess.run(['tmux', 'send-keys', '-t', 'llama1', user_input + "/", 'Enter'])
    # print(get_tmux_output())
    time.sleep(2)
    while True:
        current_output = get_tmux_output()
        if '>' in str(current_output[-2:]):
            output = current_output.split(">")[-2].split("\n")[1:]
            output = "\n".join(output)
            
            return str(output)
            
            break
        time.sleep(2)

# if __name__ == "__main__":
#     main()
#     while True:
#         prmpt = input(">> ")
#         output = chat(prmpt)
#         print(output)
