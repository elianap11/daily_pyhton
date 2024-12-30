'''
Este programa crea una función que comprueba si un nombre de usuario es válido según algunas 
reglas simples.
La función tomará un nombre de usuario como entrada y devolverá si es válido o no.
Las reglas para un nombre de usuario válido son:
El nombre de usuario debe tener entre 5 y 15 caracteres.
Debe contener solo caracteres alfanuméricos (letras y números).
Debe comenzar con una letra.

Cómo funciona el proyecto: Defina una función llamada check_username_validity que tome una
cadena (el nombre de usuario) como argumento. Dentro de la función, escriba las condiciones para verificar:
Si la longitud del nombre de usuario está entre 5 y 15 caracteres.
Si el nombre de usuario contiene solo caracteres alfanuméricos utilizando el método isalnum() integrado 
de Python.
Si el primer carácter del nombre de usuario es una letra utilizando isalpha().
Si se cumplen todas las condiciones, devuelva "Nombre de usuario válido". De lo contrario, devuelva un 
mensaje que indique por qué el nombre de usuario no es válido.
'''

def check_username_validity(username):
 
    if len(username) < 5 or len(username) > 15:
        return "El nombre de usuario debe tener entre 5 y 15 caracteres."

    # Verificar si el nombre de usuario es alfanumérico
    if not username.isalnum():
        #Este método devuelve True si todos los caracteres en la cadena son alfanuméricos 
        #(es decir, letras y números), y hay al menos un carácter; de lo contrario, devuelve False.
        return "El nombre de usuario debe contener solo caracteres alfanuméricos."

    # Verificar si el primer carácter es una letra
    #Este método devuelve True si todos los caracteres en la cadena son letras del alfabeto y 
    #hay al menos un carácter; de lo contrario, devuelve False.
    if not username[0].isalpha():
        return "El nombre de usuario debe comenzar con una letra."

    return "Usuario válido."

# Ejemplo de uso
username = input("Ingrese un nombre de usuario: ")
result = check_username_validity(username)
print(result)
        