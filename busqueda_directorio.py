'''
Crear un script de Python que busque archivos en un directorio específico en función de un término 
de búsqueda. La herramienta de búsqueda debe permitir al usuario buscar archivos por nombre o extensión
y mostrar los resultados coincidentes con sus rutas de archivo completas.

Cómo funciona el proyecto
(1) El programa comienza pidiendo al usuario que ingrese una ruta de directorio. 
(2) Después de que el usuario ingresa a un directorio (por ejemplo, /Users/as/Downloads), 
el programa le pide al usuario que ingrese un término de búsqueda (por ejemplo, “.png”). 
(3) Finalmente, el programa enumera todas las rutas de archivo contenidas en el directorio dado.
'''

import os

def buscar_archivos(directorio, termino_busqueda):
    resultados = []
    
    # Recorrer el directorio y sus subdirectorios
    for carpeta_raiz, subcarpetas, archivos in os.walk(directorio):
        for archivo in archivos:
            # Comprobar si el término de búsqueda está en el nombre del archivo o en la extensión
            if termino_busqueda.lower() in archivo.lower():
                ruta_completa = os.path.join(carpeta_raiz, archivo)
                resultados.append(ruta_completa)
    
    return resultados

def main():
    # Solicitar al usuario la ruta del directorio
    directorio = input("Ingresa la ruta del directorio: ")
    
    # Verificar que la ruta ingresada sea un directorio válido
    if not os.path.isdir(directorio):
        print("La ruta especificada no es un directorio válido.")
        return

    # Solicitar el término de búsqueda
    termino_busqueda = input("Ingresa el término de búsqueda (nombre o extensión): ")

    # Buscar archivos que coincidan con el término de búsqueda
    archivos_encontrados = buscar_archivos(directorio, termino_busqueda)

    # Mostrar los resultados
    if archivos_encontrados:
        print("\nArchivos encontrados:")
        for archivo in archivos_encontrados:
            print(archivo)
    else:
        print("No se encontraron archivos que coincidan con el término de búsqueda.")

if __name__ == "__main__":
    main()