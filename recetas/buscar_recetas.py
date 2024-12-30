'''
Crear un programa Python que tome una lista de ingredientes del usuario y muestre recetas 
que se pueden hacer con esos ingredientes.
Beneficios del aprendizaje
En este proyecto, practicarás el manejo de archivos y el análisis de datos JSON mientras buscas
recetas basadas en los ingredientes proporcionados por el usuario. Este proyecto reforzará tu 
comprensión de la lógica condicional y las estructuras de datos en Python.

Cómo funciona el programa
Se le solicita al usuario que ingrese una lista de ingredientes que tiene en casa. 
Una vez que el usuario ingresa los ingredientes, obtendrá todas las recetas que se 
pueden cocinar con esos ingredientes. Por ejemplo, dado que el usuario tenía pan, sal 
y aceite, se mostró la receta de bruschetta con aceite, ya que era la receta del archivo 
JSON que se podía preparar con los ingredientes que tenía el usuario. 
Puede utilizar este archivo JSON de muestra que contiene 21 recetas.
'''

import json

def cargar_recetas(archivo):
    # Abrir y cargar recetas desde el archivo JSON
    with open(archivo, 'r', encoding='utf-8') as file:
        return json.load(file)

def buscar_recetas(recetas, ingredientes_usuario):
    recetas_encontradas = []
    for receta in recetas:
        # Verifica si todos los ingredientes de la receta están en los ingredientes del usuario
        if any(ingrediente in ingredientes_usuario for ingrediente in receta['ingredients']):
            recetas_encontradas.append(receta['name'])
    return recetas_encontradas

def main():
    # Cargar recetas desde el archivo JSON dentro de la carpeta
    recetas = cargar_recetas('recipes.json')  # Asegúrate de que este archivo esté en la misma carpeta que dia20.py

    # Pedir al usuario que ingrese los ingredientes
    ingredientes_usuario = input("Ingresa una lista de ingredientes separados por comas: ").lower().split(',')
    ingredientes_usuario = [ingrediente.strip() for ingrediente in ingredientes_usuario]

    # Buscar recetas
    recetas_posibles = buscar_recetas(recetas, ingredientes_usuario)

    # Mostrar resultados
    if recetas_posibles:
        print("Puedes cocinar las siguientes recetas:")
        for receta in recetas_posibles:
            print(f"- {receta}")
    else:
        print("No se encontraron recetas con los ingredientes proporcionados.")

if __name__ == "__main__":
    main()