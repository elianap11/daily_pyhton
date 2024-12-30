'''
Cree un programa simple que verifique si un número dado es positivo, negativo o cero.

Resultado esperado
Cada vez que se ejecuta el programa, imprime diferentes mensajes según el signo del número.

'''

# Función principal
def verificar_numero():
    # Solicitar al usuario que ingrese un número
    numero = float(input("Ingrese un número: "))

    # Verificar si el número es positivo, negativo o cero
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

# Ejecutar la función
verificar_numero()