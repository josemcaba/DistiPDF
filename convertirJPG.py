import uuid
from pdf2image import convert_from_path
from imutils import paths
import os
from shutil import rmtree

def convierteJPG():
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

    print('\nCreado nuevo directorio y archivos:\n')

    pages = convert_from_path(fp, dpi=400, 
                              output_folder=fn, fmt='jpeg',
                              output_file='')     

    for imagePath in paths.list_images(fn):
        print(imagePath)        

    input('\nPulse ENTER para continuar')