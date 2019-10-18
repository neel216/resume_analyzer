'''
'''

from docx import Document

document = Document('./test_data/resume_template.docx')

paragraph_list = document.paragraphs
content = []

for paragraph in paragraph_list:
    content.append(paragraph.text)
