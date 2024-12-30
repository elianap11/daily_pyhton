'''
Este programa define una cadena, cuenta cuántas letras mayúsculas y minúsculas hay y muestra ambos recuentos.
Cómo funciona el proyecto
Comience su secuencia de comandos definiendo una oración como una cadena. Aquí hay un ejemplo:
text = "Esta oración tiene letras mayúsculas y minúsculas mezcladas!"
'''

# Definición de la cadena
text = "Esta Oración tiene LETRAS Mayúsculas y minúsculas Mezcladas!"

# Inicialización de contadores
mayusculas = 0
minusculas = 0

# Contar letras mayúsculas y minúsculas
for letra in text:
    if letra.isupper():  # Verificar si la letra es mayúscula
        mayusculas += 1
    elif letra.islower():  # Verificar si la letra es minúscula
        minusculas += 1

# Mostrar resultados
print(f"Hay {mayusculas} letras mayúsculas y {minusculas} letras minúsculas.")