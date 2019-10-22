#!/bin/bash
cd `dirname $0`
if [ -z "$FIRSTTIME" ]; then
    sudo easy_install pip
fi
export FIRSTITME="done"
python3 -m pip install setuptools -U
python3 -m pip install nltk
python3 -m pip install python-docx
python3 -c "import nltk; nltk.download('vader_lexicon')"
python3 interface.py