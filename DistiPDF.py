import os
from unirArchivosPDF import uneArchivos
from extraerPaginasPDF import extraePaginas
from separarPaginasPDF import separaPaginas
from convertirJPG import convierteJPG
from leerTextoPDF import leeTexto
from rotarPaginasPDF import rotaPaginas
from unirArchivosDirectorioPDF import uneArchivosDirectorio
from borrarPaginaPDF import borraPagina

def mostrar_menu(opciones):
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
        '2': ('Extraer páginas consecutivas', extraePaginas),
        '3': ('Separar páginas en archivos PDF', separaPaginas),
        '4': ('Separar páginas en imagenes JPG', convierteJPG),
        '5': ('Rotar páginas', rotaPaginas),
        '6': ('Unir todos los archivos del directorio', uneArchivos),
        '7': ('Borrar una página del archivo', borraPagina),
    }

    generar_menu(opciones) # El segundo parámetro es la opción para salir

if __name__ == '__main__':
    menu_principal()

