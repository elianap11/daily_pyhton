'''
Descripción del proyecto
Crea un programa que le pregunte al usuario sobre el clima actual y, usando un diccionario 
para la toma de decisiones, sugiera una actividad.

Comienza el script con este diccionario encima de tu script:

weather_activities = {
"1": "¡Es un día hermoso! ¿Qué tal un paseo por el parque? 🌳",
"2": "¡Clima perfecto para un día acogedor en el interior con un buen libro! 📚",
"3": "¡Quizás sea un buen momento para una taza de té reflexiva! ☕",
"4": "¡Construye un muñeco de nieve o haz una pelea de bolas de nieve! ⛄"
}
Luego, agrega más código para que el programa produzca el siguiente resultado.

Resultado esperado

(1) El programa solicita al usuario que elija 1, 2, 3 o 4 según el clima actual.

(2) Luego, el programa muestra un texto que pertenece a la opción en el diccionario que se 
proporciona más arriba.

'''

# Diccionario de actividades según el clima
weather_activities = {
    "1": "¡Es un día hermoso! ¿Qué tal un paseo por el parque? 🌳",
    "2": "¡Clima perfecto para un día acogedor en el interior con un buen libro! 📚",
    "3": "¡Quizás sea un buen momento para una taza de té reflexiva! ☕",
    "4": "¡Construye un muñeco de nieve o haz una pelea de bolas de nieve! ⛄"
}

def main():
    print("¿Qué tipo de clima tienes hoy?")
    print("1. Soleado")
    print("2. Nublado")
    print("3. Lluvioso")
    print("4. Nevado")

    while True:
        opcion = input("Elige 1, 2, 3 o 4 para recibir una sugerencia de actividad: ")

        if opcion in weather_activities:
            print(weather_activities[opcion])
            break
        else:
            print("Opción inválida. Por favor, elige 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()