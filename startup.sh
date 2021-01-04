#!/bin/bash

cd /opt/flask-project/application
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo systemctl stop app.service
sudo systemctl daemon-reload
pytest --cov=application --cov-report html