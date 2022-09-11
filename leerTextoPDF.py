import os
from PyPDF2 import PdfFileReader, PdfFileWriter
#from shutil import rmtree

def leeTexto():
    fn = input('Nombre del archivo : ')
    fp = fn + '.pdf'
    if not os.path.exists(fp):
        print('\n>>>>> No existe el archivo',fp,' <<<<<')
        input('\nPulse ENTER para continuar')
        return()

    textoCompleto = ''
    pdf_Reader = PdfFileReader(fp)
    numPaginas = pdf_Reader.getNumPages()
    for p in range(numPaginas):
        page = pdf_Reader.getPage(p)
        pageContent = page.extractText().replace('\n','')
        textoCompleto += pageContent


    with open(fn+'.txt', 'w') as archivo:
        archivo.write(textoCompleto)

    print('\nCreado el nuevo archivo   :', fn+'.txt')

    input('\nPulse ENTER para continuar')

