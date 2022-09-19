from pdf2image import convert_from_path
import os
from shutil import rmtree
from PyPDF2 import PdfFileReader

def extraePaginasJPG():
    fn = input('Nombre del archivo : ')
    fp = fn + '.pdf'
    if not os.path.exists(fp):
        print('\n>>>>> No existe el archivo',fp,' <<<<<')
        input('\nPulse ENTER para continuar')
        return()

    fn += '-JPGs'
    if os.path.exists(fn):
        rmtree(fn)
    os.mkdir(fn)

    pdf_Reader = PdfFileReader(fp,'rb')
    numPages = pdf_Reader.getNumPages()

    print('\nCreando nuevo directorio y archivos ...')

    i = 0
    lote = 5 # Convertimos de 5 en 5 paginas para evitar overflow de memoria
    for numPage in range(0, numPages, lote): 
        pages = convert_from_path(fp, dpi=350, thread_count = lote, # Un thread para cada archivo para una mas rapida conversion paralela
                                  first_page=numPage+1, last_page=numPage+lote) 

        for page in pages:
            i = i+1
            image_name = os.path.join(fn, "Page_{}.jpg".format(str(i)))  
            page.save(image_name, "JPEG")

    print('\nGenerados {} archivos JPG en el directorio {}'.format(numPages, fn))

    input('\nPulse ENTER para continuar')
