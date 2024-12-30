'''
Crear un programa que solicite al usuario que ingrese su estado de ánimo (feliz, estresado o cansado) 
y muestre un mensaje según el estado de ánimo enviado por el usuario.

Resultado esperado
(1) El programa solicita al usuario que ingrese su nombre (por ejemplo, Ardit)
(2) El programa saluda al usuario con “Hola, [nombre], ¿cómo te sientes hoy?” y muestra las opciones 
de estado de ánimo.
(3) El usuario elige un número (1, 2 o 3).
(4) Si el usuario está feliz, el programa muestra “Eso es genial, [nombre], sigue difundiendo tu alegría”.
(5) Si el usuario está estresado, el programa muestra “Respira profundamente, [nombre]. ¡Lo estás haciendo 
increíble!”
(6) Si el usuario está cansado, el programa muestra “Descansa, [nombre]. ¡Mañana es un nuevo comienzo!”
'''

# Solicitar el nombre del usuario
nombre = input("Ingresa tu nombre: ")

# Saludar al usuario
print(f"Hola, {nombre}, ¿cómo te sientes hoy?")
print("1. Feliz")
print("2. Estresado")
print("3. Cansado")

# Inicializar la elección del estado de ánimo
estado = ""

# Bucle para validar la entrada
while estado not in ["1", "2", "3"]:
    estado = input("Elige un número (1, 2 o 3): ")
    
    if estado == "1":
        print(f"Eso es genial, {nombre}, sigue difundiendo tu alegría.")
    elif estado == "2":
        print(f"Respira profundamente, {nombre}. ¡Lo estás haciendo increíble!")
    elif estado == "3":
        print(f"Descansa, {nombre}. ¡Mañana es un nuevo comienzo!")
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")