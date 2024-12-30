'''
Cree una calculadora de línea de comandos que realice operaciones matemáticas básicas como:
Suma
Sustracción
Multiplicación
División
Poder (exponenciación)

El programa solicita al usuario que ingrese una expresión (por ejemplo, 6 + 5). 
Una vez que el usuario ingresa la expresión y presiona Enter, el programa muestra 
el resultado (es decir, 11). Luego, el programa solicita nuevamente al usuario 
que ingrese otra expresión. Este bucle continúa hasta que el usuario ingresa
"salir" para salir del programa.
'''


while True:
    operacion = input("Ingrese una expresión (o 'salir' para terminar): ")
    
    if operacion.lower() == "salir":
        print("Saliendo del programa.")
        break

    # Realizamos una validación simple en caso que la expresión introducida tenga operadores válidos
    if '+' in operacion:
        numero = operacion.split('+')
        resultado = float(numero[0]) + float(numero[1])
    elif '-' in operacion:
        numero = operacion.split('-')
        resultado = float(numero[0]) - float(numero[1])
    elif '*' in operacion:
        numero = operacion.split('*')
        resultado = float(numero[0]) * float(numero[1])
    elif '/' in operacion:
        numero = operacion.split('/')
        if float(numero[1]) != 0:  # Asegurarse de no dividir por cero
            resultado = float(numero[0]) / float(numero[1])
        else:
            print("Error: No se puede dividir entre cero.")
            continue
    elif '^' in operacion:
        numero = operacion.split('^')
        resultado = float(numero[0]) ** float(numero[1])
    else:
        print("Error: Expresión no válida. Utilice +, -, *, / o ^.")
        continue

    print(f"El resultado es: {resultado}")

