from pypdf import PdfReader
from rag import addtodb
"""
downloaded the books

extract text from the pdfs 

implement into bot



"""


def pdf_to_db(pdf):
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)
    
    for i in range(number_of_pages):

        page = reader.pages[i]
        pagetext = page.extract_text()
        if(pagetext is not ""):
            addtodb(page.extract_text(), {"PageNum":i, "Book":pdf})

        print(f"Page {i} of {pdf} is finished")
    
def pdfread(pdf):
    text = ""
    
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)
    
    for i in range(number_of_pages):

        page = reader.pages[i]
        pagetext = page.extract_text()
        if(pagetext is not ""):
            text += pagetext

    
    return text



# pdfread("ww2_1.pdf")
# pdfread("ww2_2.pdf")
# pdfread("ww2_3.pdf")

