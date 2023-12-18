import PyPDF2

def convert(filename):
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages

        with open(filename + '.txt', 'w', encoding='utf-8') as out_file:
            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                text = page.extractText()
                out_file.write(text)

