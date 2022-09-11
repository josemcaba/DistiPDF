import os
from PyPDF2 import PdfFileMerger


def uneArchivosDirectorio():
    ruta = '.'
    archivoSalida = 'merged.pdf'
    
    if os.path.exists(archivoSalida):
        os.remove(archivoSalida) 

    with os.scandir(ruta) as ficheros:
        pdfs = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.pdf')]

    if len(pdfs) > 0:
        pdf_Merger = PdfFileMerger()

        for pdf in pdfs:
            pdf_Merger.append(open(pdf, 'rb'))
        
        with open(archivoSalida,'wb') as archivo:
            pdf_Merger.write(archivo)

        print('\nCreado el nuevo archivo :', archivoSalida)
    else:
        print('\nNo hay archivos PDF en el directorio')

    input('\nPulse ENTER para continuar')

