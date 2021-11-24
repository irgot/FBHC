from PyPDF2 import PdfFileReader, PdfFileWriter

import tabula


lista_tabelas = tabula.read_pdf('1.pdf', pages='all')

# file = open('2.pdf', 'rb')
# pdf_file = PdfFileReader(file)

# for num_page in range(pdf_file.numPages):
#     page = pdf_file.getPage(num_page)
#     text = str(page.extractText())
#     CNPJ_POS_START = text.find(
#         f'Page {num_page+1} of')+len(f'Page {num_page+1} of')
#     CNPJ_POS_END = CNPJ_POS_START+18
#     CNPJ = text[CNPJ_POS_START:CNPJ_POS_END]

#     T1K_POS_START = text.find('GOMA MANDIOCA DA TERRINHA') + \
#         len('GOMA MANDIOCA DA TERRINHA')+8
#     T1K_POS_END = text.find('84,00', T1K_POS_START)
#     QTD1K = text[T1K_POS_START:T1K_POS_END]
#     print(QTD1K)


# def rotate_pages(pdf_path):
#     pdf_writer = PdfFileWriter()
#     pdf_reader = PdfFileReader(pdf_path)
#     # Rotate page 90 degrees to the right
#     print(pdf_reader.getPage(0))

#     page_1 = pdf_reader.getPage(0).rotateClockwise(90)

#     pdf_writer.addPage(page_1)
#     # Rotate page 90 degrees to the left
#     page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
#     pdf_writer.addPage(page_2)
#     # Add a page in normal orientation
#     pdf_writer.addPage(pdf_reader.getPage(2))

#     with open('rotate_pages.pdf', 'wb') as fh:
#         pdf_writer.write(fh)

# if __name__ == '__main__':
#     path = '1.pdf'
#     rotate_pages(path)
