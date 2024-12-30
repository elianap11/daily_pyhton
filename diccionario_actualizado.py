'''
Este proyecto comienza con un diccionario predefinido que representa una lista de compras con cantidades:

grocery_list = {
"apples": 5,
"bananas": 2,
"milk": 1,
"bread": 1
}
Su tarea es agregar un código que actualice todos los valores del diccionario multiplicándolos por 10. Luego, 
imprima el diccionario actualizado.
'''

# Lista de compras predefinida
grocery_list = {
    "apples": 5,
    "bananas": 2,
    "milk": 1,
    "bread": 1
}

# Actualizar los valores multiplicándolos por 10
for item in grocery_list:
    grocery_list[item] *= 10

# Imprimir el diccionario actualizado
print(grocery_list)