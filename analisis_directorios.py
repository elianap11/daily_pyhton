'''
Esta aplicación de línea de comandos analiza una carpeta específica en su máquina local, 
incluidos todos sus subdirectorios. Identifica todos los archivos, los clasifica por tamaño
y genera un resumen de los archivos más grandes y el almacenamiento total utilizado. Descargue 
y descomprima estos archivos en una carpeta local para usarlos en el proyecto. 
Resultado esperado 
(1) El programa comienza solicitando al usuario que ingrese la ruta de la carpeta que desea 
analizar. En este caso, el nombre de mi carpeta es "carpeta" y se encuentra en el directorio local 
donde se encuentra el archivo .py, así que simplemente escribí el nombre de la carpeta "carpeta". 
(2) Luego, el programa imprime la cantidad total de archivos ubicados en la carpeta "carpeta" y 
todos sus subdirectorios. También calcula el almacenamiento total y luego clasifica todos los archivos
por tamaño.
'''

import os

def analyze_folder(folder_path):
    total_files = 0
    total_size = 0
    file_sizes = {}

    # Recorrer la carpeta y subcarpetas
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_size = os.path.getsize(file_path)

            # Actualizar conteos y almacenamiento total
            total_files += 1
            total_size += file_size
            file_sizes[file_path] = file_size

    # Clasificar archivos por tamaño
    sorted_files = sorted(file_sizes.items(), key=lambda x: x[1], reverse=True)

    # Imprimir resultados
    print(f"Total de archivos: {total_files}")
    print(f"Tamaño total en bytes: {total_size}")
    print("\nArchivos clasificados por tamaño:")
    for file_path, size in sorted_files:
        print(f"{file_path}: {size} bytes")

if __name__ == "__main__":
    folder_name = input("Ingrese la ruta de la carpeta que desea analizar: ")
    analyze_folder(folder_name)