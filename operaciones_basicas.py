'''
Construya un programa que le permita al usuario ingresar dos números y realizar una operación
(suma, resta, multiplicación o división). El programa realiza la operación con los dos números 
y muestra el resultado.

Cómo funciona el proyecto
El programa permite al usuario ingresar dos números (p. ej., 4 y 8). Luego, el programa le permite
ingresar una operación (p. ej., * para multiplicación). Finalmente, el programa muestra el resultado 
de la operación.
'''

number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))
operators = input("Ingrese la operación que quiere realizar (+,-,*,/): ")

if operators == "+":
    print ("El resultado es: ", number1 + number2)
elif operators == "-":
    print ("El resultado es: ", number1 - number2)
elif operators == "*":
    print ("El resultado es: ", number1 * number2)
elif operators == "/":
    print ("El resultado es: ", number1 / number2)
else:
    print("El símbolo no pertenece a una operación")