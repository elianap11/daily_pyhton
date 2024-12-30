'''
Generar un nombre de persona al azar

Cree un programa que lea una lista de nombres de un archivo de texto, elija uno al azar 
y lo muestre. Es perfecto para practicar el manejo de archivos y el trabajo con listas en Python.

Descargue el archivo de texto desde este enlace. El archivo de texto contiene 4945 nombres de personas. 

Beneficios del aprendizaje
Este proyecto trata sobre la lectura de texto de archivos, el procesamiento de datos de texto y la 
aplicación de la función random.choice() en listas, todo mientras se crea un programa que es útil y 
fácil de expandir.
'''

import random

def generate_random_name(file_path):
    # Leer nombres desde el archivo
    with open(file_path, 'r') as file:
        names = file.readlines()
    
    # Limpiar los nombres y elegir uno al azar
    names = [name.strip() for name in names if name.strip()]  # Eliminar espacios en blanco
    random_name = random.choice(names)
    
    return random_name

if __name__ == "__main__":
    # Ruta del archivo que contiene la lista de nombres
    file_path = './/names//names.txt'
    
    # Generar un nombre al azar
    random_name = generate_random_name(file_path)
    print(f'Nombre generado al azar: {random_name}')