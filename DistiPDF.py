import os
from unirArchivosPDF import uneArchivos
from extraerPaginasPDF import extraePaginasPDF
from separarPaginasPDF import separaPaginas
from extraerPaginasJPG import extraePaginasJPG
from leerTextoPDF import leeTexto
from rotarPaginasPDF import rotaPaginas
from unirArchivosDirectorioPDF import uneArchivosDirectorio
from borrarPaginaPDF import borraPagina
from borrarVariasPaginasPDF import borraVariasPaginas

def mostrar_menu(opciones):
    os.system('clear')
    print('\nManipulación de Archivos PDF')
    print('============================')
    for clave in sorted(opciones):
        print(' {} - {}'.format(clave, opciones[clave][0]))
    print(' 0 - Salir')

def leer_opcion(opciones):
    while (a := input('\nOpción: ')) not in opciones:
        if a == '0': break
        print('Opción incorrecta, vuelva a intentarlo.')        
    return a

def ejecutar_opcion(opcion, opciones):
    if opcion == '0':
        salir()
    else:
        opciones[opcion][1]()

def salir():
    print('Saliendo ...')

def generar_menu(opciones):
    opcion = None
    while opcion != '0':   # El 0 es la opcion de salida
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def menu_principal():
    opciones = {
        '1': ('Unir dos archivos', uneArchivos),
        '2': ('Unir todos los archivos del directorio', uneArchivosDirectorio),
        '3': ('Extraer páginas consecutivas', extraePaginasPDF),
        '4': ('Separar páginas en archivos PDF', separaPaginas),
        '5': ('Separar páginas en imagenes JPG', extraePaginasJPG),
        '6': ('Rotar páginas', rotaPaginas),
        '7': ('Borrar una página del archivo', borraPagina),
        '8': ('Borrar varias páginas del archivo', borraVariasPaginas),
        '9': ('Leer texto (OCR)', leeTexto)
    }

    generar_menu(opciones) # El segundo parámetro es la opción para salir

if __name__ == '__main__':
    menu_principal()

