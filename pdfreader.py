from pypdf import PdfReader




def pdfread(pdf):
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)
    page = reader.pages[53]
    text = page.extract_text()
    return text

testtext = pdfread("ww2_1.pdf")

print(testtext)