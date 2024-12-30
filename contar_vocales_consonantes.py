'''
Este programa define una cadena, cuenta cuántas vocales y consonantes hay y muestra ambos recuentos.
Cómo funciona el proyecto
Comienza tu script definiendo una oración como una cadena. Aquí tienes un ejemplo:
text = "¿Cuántas vocales y consonantes hay en esta oración?"
'''

text = "How many vowels and consonants are in this sentence?"

# Definir las vocales y consonantes en conjuntos para evitar duplicados
vowels = set("aeiouAEIOU")
consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") 

vowel_count = 0
consonant_count = 0

# Comprobar cada carácter en la cadena
for char in text:
    if char in vowels: 
        vowel_count += 1
    elif char in consonants: 
        consonant_count += 1

print(f"Vocales: {vowel_count}")
print(f"Consonantes: {consonant_count}")