# Descripción del proyecto
# Hoy crearás un programa que analiza todos los archivos de un directorio principal determinado y sus subdirectorios, 
# categorizando los archivos según su antigüedad (p. ej., creados hace menos de una semana, entre una semana y un mes 
# o más de un mes). Proporciona un informe resumido con recuentos para cada categoría y resalta los archivos más antiguos
# y más nuevos.

# Resultado esperado
# Esto es lo que genera el programa cuando ingreso la ruta de mi carpeta Descargas (p. ej., 
# “C:\Usuarios\su_nombre_de_usuario\Descargas” en Windows)

# El programa enumera la cantidad de archivos creados hace menos de una semana (17 archivos), entre una semana y un mes 
# (74 archivos) y hace más de un mes (22 archivos).

# También imprime la ruta al archivo más antiguo y al más nuevo.

import os
from datetime import datetime, timedelta

def analizar_archivos(directorio):
    menos_de_una_semana = 0
    entre_una_semana_y_un_mes = 0
    mas_de_un_mes = 0

    archivo_mas_antiguo = None
    archivo_mas_nuevo = None
    fecha_mas_antigua = None
    fecha_mas_nueva = None

    print(f"Analizando el directorio: {directorio}\n")
    
    # Recorrer el directorio y sus subdirectorios
    for root, dirs, files in os.walk(directorio):
        print(f"Archivos encontrados en {root}: {files}")
        for file in files:
            ruta_completa = os.path.join(root, file)
            fecha_creacion = os.path.getctime(ruta_completa)
            fecha_creacion_dt = datetime.fromtimestamp(fecha_creacion)

            print(f"Analizando archivo: {ruta_completa}, Fecha de creación: {fecha_creacion_dt}")

            edad_archivo = datetime.now() - fecha_creacion_dt

            if edad_archivo < timedelta(weeks=1):
                menos_de_una_semana += 1
            elif edad_archivo < timedelta(weeks=4):
                entre_una_semana_y_un_mes += 1
            else:
                mas_de_un_mes += 1

            # Determinar el archivo más antiguo y más nuevo
            if archivo_mas_antiguo is None or fecha_creacion_dt < fecha_mas_antigua:
                archivo_mas_antiguo = ruta_completa
                fecha_mas_antigua = fecha_creacion_dt
            
            if archivo_mas_nuevo is None or fecha_creacion_dt > fecha_mas_nueva:
                archivo_mas_nuevo = ruta_completa
                fecha_mas_nueva = fecha_creacion_dt

    # Imprimir el informe resumen
    print(f"\nArchivos creados hace menos de una semana: {menos_de_una_semana} archivos")
    print(f"Archivos creados entre una semana y un mes: {entre_una_semana_y_un_mes} archivos")
    print(f"Archivos creados hace más de un mes: {mas_de_un_mes} archivos")
    print(f"Archivo más antiguo: {archivo_mas_antiguo}")
    print(f"Archivo más nuevo: {archivo_mas_nuevo}")

# Pide al usuario que ingrese la ruta del directorio
directorio_usuario = input("Introduce la ruta de tu carpeta (ejemplo: C:\\Usuarios\\tu_nombre_de_usuario\\Descargas): ")
analizar_archivos(directorio_usuario)