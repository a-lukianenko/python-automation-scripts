import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter


try:
    while True:
        file_name = input('Enter the name of the file to encrypt (without \'.pdf\').'
                          '\n(It must be in the same folder with this script): ')
        if f'{file_name}.pdf' not in os.listdir():
            print(f'\nFile \'{file_name}\' was not found in the current folder!\n')
            continue
        break

    while True:
        password = input('Enter the password to encrypt your .pdf file: ')
        if not password.isalnum():
            print(f'\nPassword must contain at least 1 alphanumeric character!\n')
            continue
        break

    pdf_file = open(f'{file_name}.pdf', 'rb')
    reader = PdfFileReader(pdf_file)
    writer = PdfFileWriter()

    for i in range(reader.numPages):
        page = reader.getPage(i)
        writer.addPage(page)

    writer.encrypt(password)
    encrypted_file = f'{file_name}_encrypted.pdf'
    output = open(encrypted_file, 'wb')
    writer.write(output)
    pdf_file.close()
    output.close()
    print(f'\n{encrypted_file} has beed added.')
except EOFError:
    print('\nBye bye!')
    sys.exit(0)



