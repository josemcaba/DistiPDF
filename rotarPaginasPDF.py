import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from shutil import rmtree

def rotaPaginas():
    fn = input('Nombre del archivo : ')
    fp = fn + '.pdf'
    if not os.path.exists(fp):
        print('\n>>>>> No existe el archivo',fp,' <<<<<')
        input('\nPulse ENTER para continuar')
        return()

    multiplo90 = 1
    while multiplo90 != 0:
        rot = input('Rotacion (grados) : ')
        if rot == '':
            rot = 0
        rot = int(rot)
        multiplo90 = rot % 90 

    pdf_Reader = PdfFileReader(fp,'rb')
    pdf_Writer = PdfFileWriter()
    numPaginas = pdf_Reader.getNumPages()
    for pagina in range(numPaginas):
        pdf_Writer.addPage(pdf_Reader.getPage(pagina).rotateClockwise(rot))

    fo = fn + '_rot.pdf'       
    print('\nCreado nuevo archivo :',fo)
    with open(fo,'wb') as archivo:
        pdf_Writer.write(archivo)

    input('\nPulse ENTER para continuar')
