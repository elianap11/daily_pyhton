'''
Este programa define una cadena y cuenta cuántas vocales (a, e, i, o, u) están presentes 
en esa cadena. Luego muestra el recuento de vocales.
Cómo funciona el proyecto
Comienza tu secuencia de comandos definiendo una oración como una cadena. Aquí hay un ejemplo:
text = "Hola, ¿cuántas vocales hay en esta oración?"
'''

# vowels = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]  # Considerando vocales acentuadas
# cadena = "Hola, ¿cómo estás"
# centi = 0
# for char in cadena.lower():  # Convertimos la cadena a minúsculas para una comparación más sencilla
#     if char in vowels:  # Verificamos si el carácter está en la lista de vocales
#         centi += 1  # Incrementamos el contador
# print(f"En la cadena hay: {centi} vocales")


import re

cadena = "Hola, ¿cómo estás?"

# Utilizamos re.findall para encontrar todas las vocales en la cadena
vocales = re.findall(r'[aeiouáéíóúAEIOUÁÉÍÓÚ]', cadena)  # Contamos ambas vocales, acentuadas y minúsculas

centi = len(vocales)  # La cantidad de vocales encontradas se cuenta con len()

print(f"En la cadena hay: {centi} vocales")