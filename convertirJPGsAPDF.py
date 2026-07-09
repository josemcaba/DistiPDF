import os
from PIL import Image
import glob

def convertirJPGsAPDF():
    # Buscar todos los archivos JPG/JPEG (insensible a mayúsculas)
    patrones = ['*.jpg', '*.jpeg', '*.JPG', '*.JPEG']
    archivos = []
    for patron in patrones:
        archivos.extend(glob.glob(patron))
    
    # Eliminar duplicados (mismo archivo en distintas extensiones)
    archivos_unicos = set()
    for a in archivos:
        # Normalizar a minúsculas para comparar, pero conservar el nombre original
        clave = a.lower()
        if clave not in archivos_unicos:
            archivos_unicos.add(clave)
        else:
            # Si ya existe, se omite la duplicación
            pass
    
    # Obtener lista ordenada de nombres originales (usando el que apareció primero)
    # Para mantener orden, iteramos sobre los encontrados y si no está en un set de vistos, lo añadimos
    vistos = set()
    jpg_files = []
    for a in archivos:
        clave = a.lower()
        if clave not in vistos:
            vistos.add(clave)
            jpg_files.append(a)
    
    jpg_files.sort()  # Orden alfabético

    if not jpg_files:
        print('\nNo se encontraron archivos JPG en el directorio actual.')
        input('\nPulse ENTER para continuar')
        return

    salida = input('Nombre del archivo PDF de salida (sin extensión): ')
    if salida.strip() == '':
        salida = 'output'
    salida += '.pdf'

    images = []
    for archivo in jpg_files:
        try:
            img = Image.open(archivo)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            images.append(img)
        except Exception as e:
            print(f'Error al abrir {archivo}: {e}')

    if not images:
        print('No se pudo leer ninguna imagen.')
        input('\nPulse ENTER para continuar')
        return

    try:
        # Guardar todas las imágenes como un PDF multipágina
        images[0].save(salida, save_all=True, append_images=images[1:])
        print(f'\nCreado el archivo PDF: {salida}')
    except Exception as e:
        print(f'Error al guardar el PDF: {e}')

    input('\nPulse ENTER para continuar')