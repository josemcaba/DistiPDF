from pdf2image import convert_from_path
import os
from shutil import rmtree
from PyPDF2 import PdfFileReader

def convierte_a_JPG(pdf, dir):  # pdf=Nombre archivo PDF , np=Numero de paginas
    pdf_Reader = PdfFileReader(pdf,'rb')
    numPages = pdf_Reader.getNumPages()

    i = 0
    lote = 3 # Convertimos de 3 en 3 paginas para evitar overflow de memoria
    for numPage in range(0, numPages, lote): 
        pages = convert_from_path(pdf, dpi=300, thread_count = lote, # Un thread para cada archivo para una mas rapida conversion paralela
                                  first_page=numPage+1, last_page=numPage+lote, grayscale=True) 

        for page in pages:
            i = i+1
            image_name = os.path.join(dir, "Pagina_{}.jpg".format(str(i)))  
            page.save(image_name, "JPEG")

def extraePaginasJPG():
    entrada = input('Nombre del archivo : ')
    
    fileName = entrada + '.pdf'
    if not os.path.exists(fileName):
        print('\n>>>>> No existe el archivo',fileName,' <<<<<')
        input('\nPulse ENTER para continuar')
        return()

    print('\nCreando nuevo directorio y archivos ...') 

    directorio = entrada.upper() + '-JPGs'
    if os.path.exists(directorio):
        rmtree(directorio)
    os.mkdir(directorio)

    convierte_a_JPG(fileName, directorio)

    print('\nGenerados archivos JPG en el directorio {}'.format(directorio))

    input('\nPulse ENTER para continuar')
