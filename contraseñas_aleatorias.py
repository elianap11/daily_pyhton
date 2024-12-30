'''
Cree una aplicación de línea de comandos que genere contraseñas aleatorias seguras según las preferencias del usuario. 
El usuario puede especificar la longitud de la contraseña y si debe incluir letras mayúsculas, números y caracteres especiales. 
Este proyecto se centra en la aleatoriedad, las operaciones con cadenas y la validación de la entrada del usuario.

Resultado esperado
El programa comienza por hacerle algunas preguntas al usuario, como la longitud deseada de la contraseña y si debe incluir 
letras mayúsculas, números o caracteres especiales en la contraseña. Según las respuestas del usuario, el programa genera una 
contraseña y la imprime.
'''

import random
import string

def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_lowercase  # Siempre incluye letras minúsculas

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    
    if incluir_numeros:
        caracteres += string.digits
    
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter para la contraseña.")

    # Generar la contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    print("¡Bienvenido al Generador de Contraseñas!")
    
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña deseada (mínimo 6): "))
            if longitud < 6:
                print("La longitud de la contraseña debe ser al menos 6 caracteres.")
                continue
            
            incluir_mayusculas = input("¿Incluir letras mayúsculas? (si/no): ").lower() == 'si'
            incluir_numeros = input("¿Incluir números? (si/no): ").lower() == 'si'
            incluir_simbolos = input("¿Incluir caracteres especiales? (si/no): ").lower() == 'si'
            
            contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
            print(f"Contraseña generada: {contrasena}")

            break

        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()