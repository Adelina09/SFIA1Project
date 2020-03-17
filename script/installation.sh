#!/bin/bash

source venv/bin/activate

pip3 install flask

pip3 install flask_mysqldb

pip3 install pytest

pip3 install urllib3

source ~/.bashrc

python3 /var/lib/jenkins/workspace/pipeline1/app.py
