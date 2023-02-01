import os
from pdf2image import convert_from_path
import pytesseract
from shutil import rmtree
from imutils import paths
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def leeTexto():
    fn = input('Nombre del archivo : ')
    fp = fn + '.pdf'
    if not os.path.exists(fp):
        print('\n>>>>> No existe el archivo',fp,' <<<<<')
        input('\nPulse ENTER para continuar')
        return()

    fn += '-JPG'
    if os.path.exists(fn):
        rmtree(fn)
    os.mkdir(fn)

    print('\nLeyendo archivo ...')

    pages = convert_from_path(fp, dpi=400, 
                              output_folder=fn, fmt='jpeg',
                              output_file='')     

    textoCompleto = ''
    numPagina = 0
    for imagePath in paths.list_images(fn):
        numPagina += 1
        print('Pagina {}'.format(numPagina))
        textoCompleto += '\n>>>>>>>>>> Página ' + str(numPagina) + '\n'
        image = cv2.imread(imagePath)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # use Tesseract to OCR the image
        texto = pytesseract.image_to_string(image)
        textoCompleto += texto

    with open(fn+'.txt', 'w') as archivo:
        archivo.write(textoCompleto)

    print('\nCreado el nuevo archivo :', fn+'.txt')

    input('\nPulse ENTER para continuar')    
    