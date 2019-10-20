'''
Interface for federal resume reviewer
'''
from resumeAnalyzer.parser import Resume
from docx.opc.exceptions import PackageNotFoundError

import os


def get_page_count(resume):
    '''
    Returns the page count of a resume in string format
    '''
    appropriate = None
    pages = resume.page_count()

    if pages < 5 or pages > 7:
        appropriate = False
    else:
        appropriate = True
    
    return f'There are {pages} pages in the resume' # TODO - add code to add appropriate message?

def get_text_sentiment(resume):
    '''
    Returns the majority calculated sentiment of a resume in string format
    '''
    appropriate = None
    sentiment = resume.text_sentiment()

    if sentiment[0] == 'negative':
        appropriate = False
    elif sentiment[0] == 'positive' and sentiment[1] >= 0.5:
        appropriate = False
    else:
        appropriate = True
    
    return f'The tone of the resume is {sentiment[0]} with a value of {sentiment[1]}' # TODO - add add code to add appropriate message?


FOLDER_PATH = os.getcwd() + '\\resumes'
print('Loaded Resumes:')
for file in os.listdir(FOLDER_PATH):
    print(f'\t{file}')

while True:
    try:
        file_to_review = input('Which resume would you like to review? Be sure to type in the full file name and extension. ')
        
        resume = Resume(FOLDER_PATH + '\\' + file_to_review)
        print(get_page_count(resume))
        print(get_text_sentiment(resume))

        break
    except PackageNotFoundError:
        print("Sorry, we didn't find that file in the 'resumes' folder.\n")