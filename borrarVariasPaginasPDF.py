import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def borraVariasPaginas():
    fn = input('Nombre del archivo : ')
    fp = fn + '.pdf'
    if not os.path.exists(fp):
        print('\n>>>>> No existe el archivo',fp,' <<<<<')
        input('\nPulse ENTER para continuar')
        return()

    pdf_Reader = PdfFileReader(fp,'rb')
    numPages = pdf_Reader.getNumPages()    

    pageInicial = 0
    while (pageInicial < 1)  or (pageInicial > numPages):
        pageInicial = input('Pagina inicial borrar  : ')
        try:
            pageInicial = int(pageInicial)
        except:
            continue

    pageFinal = pageInicial
    while (pageFinal <= pageInicial)  or (pageFinal > numPages):
        pageFinal = input('Pagina final borrar  : ')
        try:
            pageFinal = int(pageFinal)
        except:
            continue

    pdf_Writer = PdfFileWriter()

    for pagina in range(0, numPages):
        if (pagina < pageInicial-1) or (pagina > pageFinal-1) :
            pdf_Writer.addPage(pdf_Reader.getPage(pagina))

    fo = fn+'_updated.pdf'
    with open(fo,'wb') as archivo:
        pdf_Writer.write(archivo)

    print('\nCreado el nuevo archivo:', fo)

    input('\nPulse ENTER para continuar')

    