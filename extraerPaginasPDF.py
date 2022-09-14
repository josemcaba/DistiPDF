import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def extraePaginasPDF():
    fn = input('Nombre del archivo : ')
    fp = fn + '.pdf'
    if not os.path.exists(fp):
        print('\n>>>>> No existe el archivo',fp,' <<<<<')
        input('\nPulse ENTER para continuar')
        return()

    pdf_Reader = PdfFileReader(fp,'rb')
    numPages = pdf_Reader.getNumPages()

    i = 0
    while (i < 1) or (ini == ''):
        ini = input('Pagina inicial: ')
        try:
            i = int(ini)
        except:
            continue

    f = 0
    while (f < i) or (fin == '') or (f > numPages):
        fin = input('Pagina final  : ')
        try:
            f = int(fin)
        except:
            continue        

    pdf_Writer = PdfFileWriter()

    for pagina in range(i-1, f):
        pdf_Writer.addPage(pdf_Reader.getPage(pagina))

    fo = fn+'_'+ini+'-'+fin+'.pdf'
    with open(fo,'wb') as archivo:
        pdf_Writer.write(archivo)

    print('\nCreado el nuevo archivo:', fo)

    input('\nPulse ENTER para continuar')
