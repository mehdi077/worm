import subprocess
import time
import sys

def kill_tmux_sessions():
    # Kill all existing tmux sessions
    subprocess.run(['tmux', 'kill-server'], stderr=subprocess.DEVNULL)

def create_and_run_llama():
    # Start a new tmux session with llama-cli
    subprocess.run(['tmux', 'new-session', '-d', '-s', 'llama'])
    subprocess.run(['tmux', 'send-keys', '-t', 'llama', 
                   './llama-cli -m /root/models/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-Q8_0-imat.gguf -cnv', 
                   'Enter'])

def get_tmux_output():
    # Get the output from tmux pane with increased buffer size
    result = subprocess.run(['tmux', 'capture-pane', '-S', '-1000', '-E', '1000', '-t', 'llama', '-p'], 
                          capture_output=True, text=True)
    return result.stdout

def send_input(user_input):
    # Send user input to tmux session
    subprocess.run(['tmux', 'send-keys', '-t', 'llama', user_input, 'Enter'])

def main():
    # Kill existing sessions and start new one
    kill_tmux_sessions()
    create_and_run_llama()
    
    # Wait for initial model loading
    time.sleep(5)
    
    while True:
        # Check output every 3 seconds
        time.sleep(1)
        current_output = get_tmux_output()
        
        # Check for the prompt indicating ready for input
        if "If you want to submit another line, end your input with" in current_output:
            # Get new input from user
            user_input = input("Enter your prompt: ")
            send_input(user_input)
            
            # Store the current position in output
            start_pos = len(current_output)
            
            # Wait and check for response
            while True:
                time.sleep(1)
                new_output = get_tmux_output()
                if ">" in new_output[start_pos:]:
                    # Extract response and remove the echoed input
                    response = new_output[start_pos:].split(">")[0].strip()
                    # Remove the first line (which contains the echoed input)
                    clean_response = '\n'.join(response.split('\n')[1:]).strip()
                    print("\nModel response:")
                    print(clean_response)
                    print("\n" + "===" + "\n")
                    break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        kill_tmux_sessions()
        sys.exit(0)