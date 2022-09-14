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

    i = 1
    lote = 5 # Convertimos de 5 en 5 paginas para evitar overflow de memoria
    for numPage in range(1, numPages, lote): 
        pages = convert_from_path(fp, dpi=350, thread_count = lote, # Un thread para cada archivo para una mas rapida conversion paralela
                                  first_page=numPage, last_page=numPage+(lote-1)) 

        for page in pages:
            image_name = os.path.join(fn, "Page_" + str(i) + ".jpg")  
            page.save(image_name, "JPEG")
            i = i+1

    print('\nGenerados {} archivos JPG en el directorio {}'.format(numPages, fn))

    input('\nPulse ENTER para continuar')
