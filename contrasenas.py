'''
Construya una aplicación de línea de comandos que evalúe la solidez de una contraseña 
ingresada por el usuario. La aplicación analizará la contraseña en función de estos 
criterios:

Longitud (al menos 8 caracteres)
Inclusión de letras mayúsculas y minúsculas, números, caracteres especiales (usando 
la biblioteca de expresiones regulares re) Detección de palabras del diccionario (el 
programa usa la biblioteca nltk para detectar si el usuario está usando alguna palabra 
común en inglés y no aceptará dichas palabras para que la contraseña sea más segura).

El programa también imprime algunas recomendaciones para proporcionar una contraseña segura.
'''

import re
import nltk
from nltk.corpus import words

# Descargadas las palabras de nltk
nltk.download('words')

def check_password_strength(password):
    # Criterios de evaluación
    length_valid = len(password) >= 8
    uppercase_valid = re.search(r'[A-Z]', password) is not None
    lowercase_valid = re.search(r'[a-z]', password) is not None
    digit_valid = re.search(r'\d', password) is not None
    special_char_valid = re.search(r'[\W]', password) is not None

    # Detección de palabras comunes
    word_list = set(words.words())
    contains_dictionary_word = any(word in word_list for word in password.split())

    # Evaluar la fortaleza de la contraseña
    if not length_valid or not uppercase_valid or not lowercase_valid or not digit_valid or not special_char_valid or contains_dictionary_word:
        strength = 'Weak'
        suggestions = []
        if not length_valid:
            suggestions.append("- Password should be at least 8 characters long.")
        if not uppercase_valid:
            suggestions.append("- Password should include both uppercase and lowercase letters.")
        if not lowercase_valid:
            suggestions.append("- Password should include both uppercase and lowercase letters.")
        if not digit_valid:
            suggestions.append("- Password should include at least one digit.")
        if not special_char_valid:
            suggestions.append("- Password should include at least one special character (!, @, #, etc.).")
        if contains_dictionary_word:
            suggestions.append("- Password should not contain common dictionary words.")
    else:
        strength = 'Strong'
        suggestions = []

    return strength, suggestions

if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    password = input("Enter your password: ")
    strength, suggestions = check_password_strength(password)

    print("Password Strength:", strength)
    if suggestions:
        print("Suggestions to improve your password:")
        for suggestion in suggestions:
            print(suggestion)