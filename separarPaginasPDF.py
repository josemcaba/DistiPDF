import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from shutil import rmtree

def separaPaginas():
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

    dc = input('Doble cara (S/N) : ')
    if dc == 'S' or dc == 's':
        dc = 2
    else:
        dc = 1

    fn += '-PDF'
    if os.path.exists(fn):
        rmtree(fn)
    os.mkdir(fn)

    print('\nCreado nuevo directorio y archivos:\n')

    pdf_Reader = PdfFileReader(fp,'rb')
    numPaginas = pdf_Reader.getNumPages()
    for pagina in range(0, numPaginas, dc):
        pdf_Writer = PdfFileWriter()
        pdf_Writer.addPage(pdf_Reader.getPage(pagina).rotateClockwise(rot))
        if (dc == 2) and (pagina < numPaginas-1):
            pdf_Writer.addPage(pdf_Reader.getPage(pagina+1).rotateClockwise(rot))
        fo = os.path.join(fn, fn+'_'+str(pagina+1)+'.pdf')
        print(fo)
        with open(fo,'wb') as archivo:
            pdf_Writer.write(archivo)

    input('\nPulse ENTER para continuar')
