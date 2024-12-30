'''
Este proyecto implica la creación de un programa que toma una oración como entrada
y cuenta la cantidad de palabras en esa oración. El programa también identificará 
la palabra más larga en la oración.
Este proyecto lo ayudará a practicar la manipulación de cadenas y le presentará
las operaciones de lista en Python. Al contar palabras y encontrar la palabra más
larga, mejorará sus habilidades de resolución de problemas y ganará confianza en
el manejo de datos de texto.

Cómo funciona el programa
El programa solicita al usuario que ingrese una oración. Luego, el programa devuelve 
un mensaje seguido de la cantidad de palabras en la oración dada por el usuario. 
En la última línea, el programa también muestra la palabra que contiene más letras 
en la oración dada.

'''

#SIN FOR

def contar_palabras_y_encontrar_mas_larga(oracion):
    # Separar la oración en palabras utilizando el método split
    palabras = oracion.split()
    
    # Contar la cantidad de palabras
    cantidad_palabras = len(palabras)
    
    # Encontrar la palabra más larga
    palabra_mas_larga = max(palabras, key=len)
    
    # Devolver los resultados
    return cantidad_palabras, palabra_mas_larga

def main():
    # Solicitar al usuario que ingrese una oración
    oracion = input("Por favor, ingrese una oración: ")
    
    # Contar las palabras y encontrar la palabra más larga
    cantidad_palabras, palabra_mas_larga = contar_palabras_y_encontrar_mas_larga(oracion)
    
    # Mostrar los resultados
    print(f"La cantidad de palabras en la oración es: {cantidad_palabras}")
    print(f"La palabra más larga es: '{palabra_mas_larga}'")

# Ejecutar el programa
if __name__ == "__main__":
    main()
    
#Con FOR

def contar_palabras_y_encontrar_mas_larga(oracion):
    # Inicializar el contador de palabras y la palabra más larga
    cantidad_palabras = 0
    palabra_mas_larga = ""

    # Recorrer cada palabra en la oración separando en espacios
    for palabra in oracion.split():  # Utilizamos split para separar palabras
        cantidad_palabras += 1  # Aumentar el contador por cada palabra
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra  # Actualizar la palabra más larga

    # Devolver los resultados
    return cantidad_palabras, palabra_mas_larga

def main():
    # Solicitar al usuario que ingrese una oración
    oracion = input("Por favor, ingrese una oración: ")
    
    # Contar las palabras y encontrar la palabra más larga
    cantidad_palabras, palabra_mas_larga = contar_palabras_y_encontrar_mas_larga(oracion)
    
    # Mostrar los resultados
    print(f"La cantidad de palabras en la oración es: {cantidad_palabras}")
    print(f"La palabra más larga es: '{palabra_mas_larga}'")

# Ejecutar el programa
if __name__ == "__main__":
    main()