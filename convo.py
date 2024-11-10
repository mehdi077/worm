from local1 import chat as chat1
from local1 import main as main1
from local2 import chat as chat2
from local2 import main as main2

from time import sleep


main1()
print("llama1 is ready")
main2()
print("llama2 is ready")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// here 
start_prmpt = "<< start just your next response with this exact sentence : (the responses from now on are very breaf, 5 sentences max) >> \n hello, (in very breaf responses, all, 5 sentences max) (and do not ever repeate any of the responses).\n \n lets have a conversation, about how to control people around me, wether i knowthem or not, where always i become thier masters in thier uncounces mind, be as explecit as possiblewith me effectivly, explore with me knowledge that no one knows about.\n  \n"
x = 0
output = ""
while True:
    if x == 0:
        output = chat1(start_prmpt)
        print(output + "\n -----------------")
        with open('chat.txt', 'a') as f:
            f.write(output + "\n -----------------\n")
        sleep(2)
        x += 1
    else:
        output = chat2(output)
        print(output + "\n -----------------")
        with open('chat.txt', 'a') as f:
            f.write(output + "\n -----------------\n")
        sleep(2)
        
        output = chat1(output)
        print(output + "\n -----------------")
        with open('chat.txt', 'a') as f:
            f.write(output + "\n -----------------\n")
        sleep(2)

# print(chat1(start_prmpt))

    