'''
Cree un programa que lea una lista de nombres de un archivo de texto, elija uno al azar y lo muestre. 
Es perfecto para practicar el manejo de archivos y el trabajo con listas en Python.
Descargue el archivo de texto desde este enlace. El archivo de texto contiene 4945 nombres de personas.
Beneficios del aprendizaje
Este proyecto trata sobre la lectura de texto de archivos, el procesamiento de datos de texto y la 
aplicación de la función random.choice() en listas, todo mientras se crea un programa que es útil y 
fácil de expandir.
'''

import random

def leer_nombres(archivo):
    """Lee los nombres desde un archivo de texto."""
    with open(archivo, 'r') as file:
        # Lee todas las líneas y elimina los caracteres de nueva línea
        nombres = [linea.strip() for linea in file]
    return nombres

def seleccionar_nombre(nombres):
    """Selecciona un nombre aleatorio de la lista."""
    return random.choice(nombres)

def main():
    archivo = './/names2//names.txt'  # Asegúrate de que la ruta sea correcta
    nombres = leer_nombres(archivo)
    
    if nombres:
        nombre_seleccionado = seleccionar_nombre(nombres)
        print(f"Nombre seleccionado al azar: {nombre_seleccionado}")
    else:
        print("No se encontraron nombres en el archivo.")

if __name__ == "__main__":
    main()