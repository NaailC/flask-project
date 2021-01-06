#!/bin/bash


sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo systemctl daemon-reload
