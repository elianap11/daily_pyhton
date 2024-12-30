'''
Escriba un programa que tome una lista de palabras y encuentre la palabra más larga de esa lista. 
El programa también debería mostrar la longitud de esa palabra.

Comience colocando la siguiente lista en su script:

words = ["apple", "banana", "cherry", "blueberry"]
A continuación se muestra lo que debería mostrar su programa.

Como puede ver arriba, el programa ha encontrado la palabra más larga y ha impreso un mensaje que 
también incluye la longitud de la palabra más larga. Se recomienda utilizar una f-string para 
construir ese mensaje.
'''

# Lista de palabras
words = ["apple", "banana", "cherry", "blueberry"]

# Encontrar la palabra más larga
longest_word = max(words, key=len)

# Obtener la longitud de la palabra más larga
length_of_longest_word = len(longest_word)

# Imprimir el resultado con f-string
print(f"La palabra más larga es '{longest_word}' y su longitud es {length_of_longest_word}.")