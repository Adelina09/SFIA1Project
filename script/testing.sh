#!/bin/bash

source /var/lib/jenkins/workspace/pipeline1/venv/bin/activate

coverage run -m pytest ./test/testing.py

coverage report