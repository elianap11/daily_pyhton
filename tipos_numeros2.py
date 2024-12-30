'''
En un proyecto anterior, creamos un programa que verificaba si un número era positivo o negativo, o cero:

number = float(input("Ingrese un número: "))

if number > 0:
print("El número es positivo")
elif number < 0:
print("El número es negativo")
else:
print("El número es cero")
En este proyecto, su tarea es mejorar ese proyecto mediante:

(1) Realizar las verificaciones dentro de una definición de función y luego llamar a esa función.

(2) Incluir el número en los mensajes (p. ej., "El número -5 es negativo") como se muestra en la sección.
'''

# Definición de la función para verificar el número
def verificar_numero():
    number = float(input("Ingrese un número: "))

    if number > 0:
        print(f"El número {number} es positivo")
    elif number < 0:
        print(f"El número {number} es negativo")
    else:
        print(f"El número {number} es cero")

# Llamada a la función
verificar_numero()