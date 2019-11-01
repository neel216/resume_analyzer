'''
Instructions to setup resume reviewer [WINDOWS ONLY]
1. Make sure Python is installed. Download the lastest version of Python 3.7 here if you haven't already: https://www.python.org/downloads/
2. Run this file (setup.py)
3. Run reviewer.py to use the resume reviewer

This file installs the required dependencies for the resume reviewer.
'''
import os

# If running the reviewer for the first time
if 'placeHolder.txt' in os.listdir('resumes/'):
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

    nltk.download('vader_lexicon') # Load nltk library for sentiment analysis
    os.remove('resumes/placeHolder.txt') # Delete placeholder file in resumes folder
else:
    print('Loaded dependencies.')
