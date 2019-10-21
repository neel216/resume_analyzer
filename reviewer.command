#!/bin/bash
cd `dirname $0`
sudo easy_install pip
python3 -m pip install setuptools -U
python3 -m pip install nltk
python3 -m pip install python-docx
python3 setup.py
python3 interface.py
