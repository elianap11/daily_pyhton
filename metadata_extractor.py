# Su herramienta de línea de comandos de Python extrae metadatos de archivos en un 
# directorio específico y los muestra. Los metadatos incluyen el tamaño del archivo, 
# la fecha de creación, la fecha de modificación y el tipo de archivo. Los usuarios 
# pueden ver una lista de todos los archivos en un directorio, incluidos los archivos
# en subdirectorios, junto con sus metadatos. Los resultados también se pueden guardar
# en un archivo CSV para su uso o análisis posterior.

# Cómo funciona el programa
# El programa permite al usuario ingresar una ruta de directorio en la terminal donde se encuentran 
# algunos archivos (por ejemplo, /Users/as/Downloads/myfolder para Mac/Linux o 
# C:\Users\as\Downloads\myfolder para Windows)
# El programa muestra la lista de rutas de archivos contenidas en el directorio dado y sus metadatos
# (tamaño, fecha de creación y tipo).
# El programa también permite al usuario elegir si desea guardar los resultados de los metadatos en 
# un archivo CSV o no:

# Consejo: Puede extraer la hora y el tamaño de creación del archivo utilizando la biblioteca del 
# sistema operativo.

# tiempo_creación = os.path.getctime(ruta_archivo)
# tiempo_modificación = os.path.getmtime(ruta_archivo)


import os
import csv
import argparse
from datetime import datetime
import mimetypes
import sys
from pathlib import Path

def extraer_metadatos(ruta):
    metadatos = []
    try:
        for entry in os.scandir(Path(ruta).resolve()):
            if entry.is_file():
                stats = entry.stat()
                tipo_archivo = mimetypes.guess_type(entry.path)[0] or 'desconocido'
                metadatos.append([
                    entry.path,
                    f"{stats.st_size:,}",
                    datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
                    datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                    tipo_archivo
                ])
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    return metadatos

def mostrar_metadatos(metadatos):
    if not metadatos:
        print("No se encontraron archivos")
        return
    
    for dato in metadatos:
        print("\n".join(f"{campo}: {valor}" for campo, valor in zip(
            ['Ruta', 'Tamaño (bytes)', 'Creado', 'Modificado', 'Tipo'],
            dato
        )))
        print()

def guardar_csv(metadatos, archivo):
    try:
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Ruta', 'Tamaño (bytes)', 'Fecha creación', 'Fecha modificación', 'Tipo'])
            writer.writerows(metadatos)
        print(f'Metadatos guardados en {archivo}')
    except IOError as e:
        print(f"Error al guardar CSV: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Extractor de metadatos de archivos')
    parser.add_argument('ruta', help='Ruta del directorio')
    parser.add_argument('--guardar', help='Nombre del archivo CSV de salida')
    args = parser.parse_args()

    metadatos = extraer_metadatos(args.ruta)
    mostrar_metadatos(metadatos)
    if args.guardar:
        guardar_csv(metadatos, args.guardar)

if __name__ == '__main__':
    main()