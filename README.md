10 november 2024
llama1 ssh root@172.232.34.167
llama2 ssh root@172.232.34.231

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y build-essential git cmake wget
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
mkdir ../models
cd ../models
wget -c https://huggingface.co/LWDCLS/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-GGUF-IQ-Imatrix-Request/resolve/main/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-Q8_0-imat.gguf


apt install python3-pip -y
apt install python3.12-venv -y
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn requests pydantic

sudo ufw allow 5000

ssh-keygen -t rsa -b 2048
ssh-copy-id root@172.232.34.167


vim modelfile
FROM ./models/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-Q8_0-imat.gguf
ollama create darkidol -f modelfile


Install GitHub CLI	sudo apt install gh
Log in	gh auth login
Create project directory	mkdir my-project && cd my-project
Initialize git repo	git init
Stage files	git add .
Commit changes	git commit -m "Initial commit"
Create & push repo	gh repo create my-newrepo --public --source=. --remote=upstream --push
Add remote (existing repo)	git remote add origin https://github.com/username/my-newrepo.git
Push changes	git push -u origin master