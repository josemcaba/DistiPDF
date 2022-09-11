import os
from unirArchivosPDF import uneArchivos
from extraerPaginasPDF import extraePaginas
from separarPaginasPDF import separaPaginas
from convertirJPG import convierteJPG
from leerTextoPDF import leeTexto
from rotarPaginasPDF import rotaPaginas
from unirArchivosDirectorioPDF import uneArchivosDirectorio
from borrarPaginaPDF import borraPagina

while True:
    os.system('cls')
    print('\nManipulación de Archivos PDF (V1.0)')
    print(  '===================================\n')

    print('1 - Unir dos archivos')
    print('2 - Extraer páginas consecutivas')
    print('3 - Separar páginas en archivos PDF')
    print('4 - Separar páginas en imagenes JPG')
    print('5 - Rotar páginas')
    print('6 - Unir todos los archivos del directorio')
    print('7 - Borrar una página del archivo')
    print('0 - Salir')

    print('\nSeleccione opción: ', end='')

    opcion = input()
    if (opcion == '1'):
        print('\nUnir dos archivos')
        print(  '-----------------')
        uneArchivos()
    elif (opcion == '2'):
        print('\nExtraer páginas consecutivas')
        print(  '----------------------------')
        extraePaginas() 
    elif (opcion == '3'):
        print('\nSeparar en archivos PDF')
        print(  '-----------------------')
        separaPaginas()
    elif (opcion == '4'):
        print('\nSeparar páginas en imagenes JPG')
        print(  '-------------------------------')
        convierteJPG()
    elif (opcion == '5'):
        print('\nRotar páginas')
        print(  '-------------')
        rotaPaginas()
    elif (opcion == '6'):
        print('\nUnir los archivos del directorio')
        print(  '--------------------------------')
        uneArchivosDirectorio()
    elif (opcion == '7'):
        print('\nBorrar una página del archivo')
        print(  '-----------------------------')
        borraPagina()   
    elif (opcion == '0'):
        print('Adios')
        break

