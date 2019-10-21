'''
Interface for federal resume reviewer
'''
from resumeAnalyzer.parser import Resume, PAGE_COUNT_ALLOWED
from docx.opc.exceptions import PackageNotFoundError

import os


def get_page_count(resume):
    '''
    Returns the page count of a resume in string format
    '''
    change = ''
    pages = resume.page_count()

    if pages < 5:
        change = ' The resume should have more pages/length.'
    elif pages > 7:
        change = ' The resume should have fewer pages and less length.'
    
    return f'There are {pages} pages in the resume.{change}'

def get_text_sentiment(resume):
    '''
    Returns the majority calculated sentiment of a resume in string format
    '''
    change = ' The resume has an appropriate tone.'
    sentiment = resume.text_sentiment()

    if sentiment[0] == 'negative':
        change = ' The resume should have a more positive tone.'
    elif sentiment[0] == 'positive' and sentiment[1] >= 0.5:
        change = ' The resume should have a slightly less positive tone.'
    
    return f'The tone of the resume is {sentiment[0]} with a value of {sentiment[1]}.{change}'

def correct_spelling(resume):
    '''
    Corrects the spelling of a resume
    '''
    misspelled_words = resume.spell_check()

    return f'Corrected {misspelled_words} misspelled words in the resume.'


if PAGE_COUNT_ALLOWED == True:
    FOLDER_PATH = os.getcwd() + '\\resumes'
else:
    FOLDER_PATH = os.getcwd() + '/resumes'

while True:
    # Print resume files in resumes directory
    print('\nLoaded Resumes:')
    if len(os.listdir(FOLDER_PATH)) == 0:
        print("Did not detect any resumes. Close this window, add any resumes you want to review to the 'resumes' folder, then run this file to review them.")
        input('')
    else:
        for file in os.listdir(FOLDER_PATH):
            print(f'\t{file}')

        try:
            file_to_review = input('\nWhich resume would you like to review? Be sure to type in the full file name and extension. ')

            resume = Resume(FOLDER_PATH + '\\' + file_to_review)
            if PAGE_COUNT_ALLOWED == True:
                print('---- ' + get_page_count(resume))
            print('---- ' + get_text_sentiment(resume))
            print('---- ' + correct_spelling(resume))

        except PackageNotFoundError:
            print("Sorry, we didn't find that file in the 'resumes' folder.\n")