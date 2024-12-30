'''
Crea un programa que lea una lista de citas motivacionales de un archivo de texto y seleccione 
una para mostrar todos los lunes (o cualquier día en que el usuario ejecute el programa). 
Utiliza el manejo de fecha de Python para verificar el día actual y garantiza que recibas una 
nueva cita cada vez que lo ejecutes.
Resultado esperado
A) Escenario 1: Si es lunes. El programa verifica qué día es. Si es lunes, muestra otro texto 
como se muestra arriba y elige una cita del archivo quotes.txt.
B) Escenario 2: Si no es lunes. Si no es lunes, el programa muestra otro texto: "Today is Tuesday".

Beneficios del aprendizaje
Manejo de archivos: Practicará la lectura de datos de un archivo, una habilidad fundamental para 
trabajar con recursos externos como bases de datos, registros o archivos de configuración. 
Aleatorización: Practicará el uso del módulo aleatorio para generar resultados impredecibles, 
algo común en aplicaciones como juegos, recomendaciones y herramientas creativas. Procesamiento 
de cadenas: Practicará el análisis y la manipulación de cadenas, como cortar, eliminar espacios 
en blanco y formatear texto para una mejor legibilidad. Flujo de control: Practicará estructuras 
lógicas como if-else para tomar decisiones basadas en la entrada del usuario, un aspecto central 
de los programas interactivos. Formato de salida: Practicará la creación de salidas de consola 
fáciles de usar, una habilidad valiosa para hacer que sus programas sean atractivos y fáciles de 
usar.
'''

import random
from datetime import datetime

# Función para leer citas desde un archivo
def read_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        quotes = file.readlines()
    return [quote.strip() for quote in quotes if quote.strip()]

# Verificar si hoy es lunes
def is_monday():
    return datetime.now().weekday() == 0  # 0 es lunes

# Función principal
def main():
    quotes_file = './/citas//quotes.txt'
    quotes = read_quotes(quotes_file)

    if is_monday():
        # Si es lunes, elige una cita aleatoria
        quote = random.choice(quotes)
        print(f"Hoy es lunes! Aquí tienes una cita motivacional: \n\"{quote}\"")
    else:
        print("Hoy no es lunes. ¡Sigue aprendiendo y mantén el espíritu motivado!")

# Ejecutar el programa
if __name__ == "__main__":
    main()