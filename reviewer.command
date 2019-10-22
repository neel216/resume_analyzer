#!/bin/bash
cd "$(dirname "$0")"
cd resumes

if [ hash .gitignore 2>/dev/null ]; then
    echo "Installing dependencies."
    cd ..
    sudo easy_install pip
    python3 -m pip install setuptools -U
    python3 -m pip install nltk
    python3 -m pip install python-docx

    cd /Applications/"Python 3.7"
    open "Install Certificates.command"
    sleep 3

    cd "$(dirname "$0")"
    python3 -c "import nltk; nltk.download('vader_lexicon')"
    rm ./resumes/.gitignore
fi

echo "Done loading dependences."

cd "$(dirname "$0")"
python3 interface.py
