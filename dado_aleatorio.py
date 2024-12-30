'''
Este proyecto simula el lanzamiento de un dado generando un número aleatorio entre 1 y 6. 
Cada vez que se ejecuta el programa, "lanza los dados" y muestra el resultado. Este proyecto 
presenta a los estudiantes el trabajo con números aleatorios y el formato de salida básico.

Cómo funciona el proyecto
El programa utilizará el módulo aleatorio de Python para simular el lanzamiento de un dado de seis caras. 
Cada vez que se ejecuta el programa, muestra un mensaje que contiene el número aleatorio.
'''
import random

print("Lanzando el dado")

resultado = random.randint(1, 6)

print(f"El resultado es: {resultado}")