'''
Interface for federal resume reviewer
'''
from resumeAnalyzer.parser import Resume


def resume_review(file_path):
    return Resume(file_path)

def get_page_count(resume):
    appropriate = None
    pages = resume.page_count()

    if pages < 5 or pages > 7:          # TODO - check email to see if page limits are correct
        appropriate = False
    else:
        appropriate = True
    
    return pages, appropriate

def get_text_sentiment(resume):
    appropriate = None
    sentiment = resume.text_sentiment()

    if sentiment[0] == 'negative':
        appropriate = False
    elif sentiment[0] == 'positive' and sentiment[1] >= 0.5:
        appropriate = False
    else:
        appropriate = True
    
    return sentiment[0], appropriate    # TODO - convert to string?

print('run')
