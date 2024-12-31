'''
En un proyecto anterior para principiantes, creamos un programa que identificaba 
la palabra más larga de una lista dada. El programa de hoy es una versión avanzada 
de la versión para principiantes, ya que obtiene los elementos de la lista del usuario
a través de la entrada del usuario en lugar de tener las listas codificadas en el programa.

En concreto, el programa:
Permite al usuario introducir una lista de palabras en la terminal y especificar la palabra 
mínima. Identifica la(s) palabra(s) más larga(s) de la lista, incluidas varias palabras con 
la misma longitud máxima, e imprime un mensaje que incluye la cantidad de caracteres de esa 
palabra.
'''

def encontrar_palabras_largas():

    lista_palabras = input("Introduce una lista de palabras (separadas por espacios): ").split()
    longitud_minima = int(input("Especifica la longitud mínima: "))

    # Filtrar palabras por la longitud mínima
    palabras_filtradas = [palabra for palabra in lista_palabras if len(palabra) >= longitud_minima]

    if not palabras_filtradas:
        print("No hay palabras que cumplan con la longitud mínima especificada.")
        return

    # Encontrar la longitud máxima
    longitud_maxima = max(len(palabra) for palabra in palabras_filtradas)

    # Obtener la(s) palabra(s) más larga(s)
    palabras_mas_largas = [palabra for palabra in palabras_filtradas if len(palabra) == longitud_maxima]

    # Imprimir el resultado
    print(f"La(s) palabra(s) más larga(s): {', '.join(palabras_mas_largas)} ({longitud_maxima} caracteres)")


encontrar_palabras_largas()