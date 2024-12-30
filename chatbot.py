'''
Crear un chatbot básico que pueda responder a un conjunto limitado de preguntas o palabras clave. 
Este chatbot analizará la entrada del usuario y dará respuestas predefinidas en función de las palabras 
clave que detecte.

Beneficios del aprendizaje
En este proyecto, mejorará su comprensión del flujo de control y las estructuras de datos mediante la 
creación de un chatbot que utiliza diccionarios para el mapeo de palabras clave y respuestas. Esto también 
le brindará experiencia práctica con el manejo de entradas del usuario y la manipulación de cadenas.

Cómo funciona el programa
El programa comienza saludando al usuario y haciéndole saber que puede escribir "adiós" para salir del programa.
El usuario puede hacer preguntas simples como "¿qué hora es?" o "¿qué es Python?" y el chatbot responde. Las 
respuestas se obtienen de un diccionario de Python dentro del script:

# Define algunas respuestas para las palabras clave
responses = {
"hello": "¡Hola! ¿En qué puedo ayudarte hoy?",
"hi": "¡Hola! ¿Qué tienes en mente?",
"weather": "No estoy seguro del clima, pero siempre es un buen día para programar".,
"time": f"La hora actual es {datetime.datetime.now().strftime('%H:%M')}.",
"day": f"Hoy es {datetime.datetime.now().strftime('%A')}.",
"python": "Python es un lenguaje de programación versátil, ideal para el desarrollo web, la ciencia de datos y más.",
"bye": "¡Adiós! ¡Que tengas un excelente día!",
}
Puedes comenzar con el diccionario anterior e implementar el resto del programa.

'''

import datetime

# Define algunas respuestas para las palabras clave
responses = {
    "hello": "¡Hola! ¿En qué puedo ayudarte hoy?",
    "hi": "¡Hola! ¿Qué tienes en mente?",
    "weather": "No estoy seguro del clima, pero siempre es un buen día para programar.",
    "time": f"La hora actual es {datetime.datetime.now().strftime('%H:%M')}.",
    "day": f"Hoy es {datetime.datetime.now().strftime('%A')}.",
    "python": "Python es un lenguaje de programación versátil, ideal para el desarrollo web, la ciencia de datos y más.",
    "bye": "¡Adiós! ¡Que tengas un excelente día!",
}

def chatbot():
    print("¡Hola! Soy un chatbot. Escribe 'adiós' para salir.")
    
    while True:
        user_input = input("Tú: ").lower()  # Entrada del usuario en minúsculas
        
        if user_input in responses:
            print("Chatbot:", responses[user_input])
            if user_input == "bye":
                break  # Sale del bucle si el usuario dice "adiós"
        else:
            print("Chatbot: Lo siento, no entiendo esa pregunta. ¿Puedes reformularla?")

# Ejecuta el chatbot
chatbot()