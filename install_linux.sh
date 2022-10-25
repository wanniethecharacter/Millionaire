#!/bin/bash
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
sudo apt install python3-pip
sudo apt install pythonpy
pip install pipreqs
pipreqs .
pip install -r requirements.txt
path_to_millionaire=$(echo readlink -f ../millionaire/runner.py)
cd ./bin || exit
cat <<EOF > millionaire.sh
#!/bin/bash
python3 $($path_to_millionaire)
EOF