#!/bin/bash


sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
sudo systemctl daemon-reload
pytest --cov=application --cov-report html