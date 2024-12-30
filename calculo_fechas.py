'''
Descripción del proyecto
Este programa le ayuda a realizar un seguimiento de los plazos al permitirle ingresar 
una fecha y hora específicas. Calcula si el plazo ya ha pasado, si es hoy o cuántos días 
faltan para la fecha límite.

Resultado esperado
A) Escenario 1: Fecha límite no vencida
El programa comienza solicitando al usuario que ingrese una fecha límite en el formato 
AAAA-MM-DD HH:MM. Si la fecha límite de envío es posterior a la fecha y hora actuales, el 
programa muestra el mensaje “La fecha límite es en x día(s). Siga trabajando 🚀”

B) Escenario 2: Fecha límite vencida
Si la fecha de envío es anterior a la fecha de hoy, eso significa que la fecha límite ha 
pasado y se imprime el mensaje “La fecha límite ha pasado 😢”.
'''

from datetime import datetime

def verificar_fecha_limite():
    # Solicitar la fecha límite al usuario
    fecha_limite_input = input("Ingrese la fecha límite (formato AAAA-MM-DD HH:MM): ")
    
    # Convertir la entrada a un objeto datetime
    try:
        fecha_limite = datetime.strptime(fecha_limite_input, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Formato de fecha inválido. Asegúrese de usar AAAA-MM-DD HH:MM.")
        return

    # Obtener la fecha y hora actuales
    fecha_actual = datetime.now()

    # Ignorar la hora para la comparación
    if fecha_limite.date() > fecha_actual.date():
        # Calcular cuántos días faltan para la fecha límite
        diferencia = (fecha_limite - fecha_actual).days
        print(f"La fecha límite es en {diferencia} día(s). Siga trabajando 🚀")
    elif fecha_limite.date() < fecha_actual.date():
        print("La fecha límite ha pasado 😢")
    else:
        print("La fecha límite es hoy. ¡Buena suerte!")

# Ejecutar la función
verificar_fecha_limite()