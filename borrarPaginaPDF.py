import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def borraPagina():
    fn = input('Nombre del archivo : ')
    fp = fn + '.pdf'
    if not os.path.exists(fp):
        print('\n>>>>> No existe el archivo',fp,' <<<<<')
        input('\nPulse ENTER para continuar')
        return()

    pdf_Reader = PdfFileReader(fp,'rb')
    numPages = pdf_Reader.getNumPages()    

    p = 0
    while (p < 1)  or (p > numPages):
        p = input('Pagina a borrar  : ')
        try:
            p = int(p)
        except:
            continue

    pdf_Writer = PdfFileWriter()

    for pagina in range(0, numPages):
        if pagina != p-1:
            pdf_Writer.addPage(pdf_Reader.getPage(pagina))

    fo = fn+'_updated.pdf'
    with open(fo,'wb') as archivo:
        pdf_Writer.write(archivo)

    print('\nCreado el nuevo archivo:', fo)

    input('\nPulse ENTER para continuar')

    