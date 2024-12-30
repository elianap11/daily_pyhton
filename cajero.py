'''
Cree un programa de simulación de cajero automático simplificado en el que el usuario 
interactúe con una interfaz similar a la de un cajero automático a través de la línea 
de comandos. El usuario puede realizar transacciones básicas, como consultar su saldo, 
depositar dinero y retirar dinero.

Descripción del proyecto
Cree un programa de simulación de cajero automático simplificado en el que el usuario 
interactúe con una interfaz similar a la de un cajero automático a través de la línea 
de comandos. El usuario puede realizar transacciones básicas, como consultar su saldo, 
depositar dinero y retirar dinero.

Así es como funciona el programa:
(1) El programa comienza con un saldo predeterminado de $100 y muestra las opciones 
(p. ej., consultar saldo, depósito, etc.)
(2) El usuario elige un número de opción (p. ej., 3 para depositar) y luego sigue las 
instrucciones (p. ej., ingresa un monto de depósito).
(3) El programa calcula el saldo actualizado e imprime nuevamente los mensajes y el saldo
actualizado.

Beneficios del aprendizaje
Este proyecto ayuda a los principiantes a comprender los fundamentos de las declaraciones 
condicionales y los bucles en Python mediante la simulación de procesos de toma de decisiones
de la vida real. El programa también puede incluir opcionalmente un manejo básico de errores.
Además, los usuarios obtienen información sobre cómo administrar y actualizar variables de 
manera dinámica en función de las acciones del usuario.

'''

def atm_simulation():
    # Saldo inicial
    balance = 100.0

    print("¡Bienvenido al cajero automático!")
    
    while True:
        # Mostrar el saldo actual y las opciones
        print(f"\nSaldo actual: ${balance:.2f}")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        
        # Obtener la opción del usuario
        option = input("Elija una opción: ")

        if option == "1":
            print(f"Su saldo actual es: ${balance:.2f}")

        elif option == "2":
            deposit_amount = float(input("Ingrese el monto a depositar: "))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"Depósito exitoso. Su nuevo saldo es: ${balance:.2f}")
            else:
                print("El monto debe ser mayor que 0.")

        elif option == "3":
            withdraw_amount = float(input("Ingrese el monto a retirar: "))
            if 0 < withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"Retiro exitoso. Su nuevo saldo es: ${balance:.2f}")
            else:
                print("Monto inválido. Asegúrese de que su saldo sea suficiente y el monto sea mayor que 0.")

        elif option == "4":
            print("Gracias por usar el cajero automático. ¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción de la lista.")

# Ejecutar la simulación
atm_simulation()