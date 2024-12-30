'''
Cree un script de Python que organice los archivos de un directorio en carpetas según el tipo de archivo.
Por ejemplo, todos los archivos .txt van a una carpeta "Archivos de texto", todos los archivos .jpg y .png 
van a una carpeta "Imágenes", y así sucesivamente.
Esto es lo que debe hacer el script paso a paso:
Use glob para buscar archivos:
Use el módulo glob para buscar todos los archivos en el directorio de destino con patrones específicos (como *.txt para archivos de texto).
Cree carpetas según el tipo de archivo:
Para cada tipo de archivo, cree una carpeta correspondiente (por ejemplo, "Archivos de texto", "Imágenes").
Mueva los archivos a la carpeta adecuada:
Mueva los archivos a la carpeta adecuada según su extensión usando shutil.move().
'''
import os
import glob
import shutil

def organizar_archivos(directorio):
    # Definir los tipos de archivo y sus carpetas de destino
    tipos_archivos = {
        'Archivos de texto': '*.txt',
        'Imágenes': ['*.jpg', '*.jpeg', '*.png'],
        'Documentos': ['*.pdf', '*.docx'],
        'Otros': '*.*'  # Para cualquier otro tipo de archivo
    }
    
    # Cambiar al directorio especificado
    os.chdir(directorio)
    
    # Crear carpetas si no existen
    for carpeta, patrones in tipos_archivos.items():
        # Si la entrada es una lista, maneja cada patrón
        if isinstance(patrones, list):
            for patron in patrones:
                crear_carpeta(carpeta)  # Crea la carpeta si no existe
                mover_archivos(patron, carpeta)
        else:
            crear_carpeta(carpeta)  # Crea la carpeta si no existe
            mover_archivos(patrones, carpeta)

def crear_carpeta(carpeta):
    """Crea la carpeta si no existe."""
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f'Carpeta creada: {carpeta}')

def mover_archivos(patron, carpeta_destino):
    """Mueve los archivos según el patrón especificado a la carpeta de destino."""
    for archivo in glob.glob(patron):
        shutil.move(archivo, carpeta_destino)
        print(f'Movido: {archivo} a {carpeta_destino}')

# Directorio a organizar
directorio_a_organizar = 'D:\usuario\Downloads\Daily Python\dia11'  # Especifica la ruta a tu directorio
organizar_archivos(directorio_a_organizar)
