'''
Instructions to setup resume reviewer
1. Make sure Python is installed. Download the lastest version here if you haven't already: https://www.python.org/downloads/
2. Run this file (setup.py)
3. Run reviewer.py to use the resume reviewer

This file installs the required dependencies for the resume reviewer.
'''
import pip
from pip._internal import main as pipmain

def install(package):
    '''
    Installs the specified Python package using pip
    '''
    if hasattr(pip, 'main'):
        pipmain(['install', package])
    else:
        pip._internal.main(['install', package])

# Download requirements from requirements.txt
with open('requirements.txt', 'r') as reqs:
    deps = reqs.read().split('\n')
for dep in deps:
    install(dep)


import nltk
import os

nltk.download('vader_lexicon') # Load nltk library for sentiment analysis
os.remove('resumes/.gitignore') # Delete .gitignore in resumes folder