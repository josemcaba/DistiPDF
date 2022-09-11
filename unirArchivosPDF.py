import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def uneArchivos():
    fn1 = input('Nombre del primer archivo : ')
    fp1 = fn1 + '.pdf'
    if not os.path.exists(fp1):
        print('\n>>>>> No existe el archivo',fp1,' <<<<<')
        input('\nPulse ENTER para continuar')
        return()

    fn2 = input('Nombre del segundo archivo: ')
    fp2 = fn2 + '.pdf'
    if not os.path.exists(fp2):
        print('\n>>>>> No existe el archivo',fp2,' <<<<<')
        input('\nPulse ENTER para continuar')
        return()

    pdf_Writer = PdfFileWriter()

    pdf_Reader = PdfFileReader(fp1,'rb')
    for pagina in range(pdf_Reader.getNumPages()):
        pdf_Writer.addPage(pdf_Reader.getPage(pagina))

    pdf_Reader = PdfFileReader(fp2,'rb')
    for pagina in range(pdf_Reader.getNumPages()):
        pdf_Writer.addPage(pdf_Reader.getPage(pagina))
        
    fo = fn1+'_'+fn2+'.pdf'
    with open(fo,'wb') as archivo:
        pdf_Writer.write(archivo)

    print('\nCreado el nuevo archivo   :', fo)

    input('\nPulse ENTER para continuar')
