'''
'''

from docx import Document


class Resume:

    def __init__(self, path):
        document = Document(path)

        paragraph_list = document.paragraphs
        self.content = []

        for paragraph in paragraph_list:
            self.content.append(paragraph.text)

    def print_content(self):
        print(self.content)
    



#document = Document('./test_data/resume_template.docx')

#paragraph_list = document.paragraphs
#content = []

#for paragraph in paragraph_list:
#    content.append(paragraph.text)

#print(content)

if __name__ == "__main__":
    resume = Resume('./test_data/resume_template.docx')
    resume.print_content()