#!/bin/bash

source /var/lib/jenkins/workspace/pipeline1/venv/bin/activate

source /var/lib/jenkins/.bashrc

coverage run -m pytest ./test/testing.py

coverage report