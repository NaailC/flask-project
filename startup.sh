sudo mkdir flaskproject 
sudo apt-get install python3-venv -y
sudo chown -R /flaskproject
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py 