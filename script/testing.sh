#!/bin/bash

source venv/bin/activate

coverage run -m pytest ./test/testing.py

coverage report -m