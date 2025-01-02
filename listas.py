'''
Las listas son uno de los tipos de datos más utilizados en Python. Están diseñados 
para almacenar muchos otros tipos de datos de Python, como números, cadenas y cualquier 
otro tipo. Para la tarea de hoy, necesita procesar las dos listas siguientes:

lista1 = [5, 3, 8, 6, 3]
lista2 = [7, 2, 5, 9, 8]

Específicamente, su tarea es:
Agregue algún código que combine las dos listas en una sola.
Elimina cualquier duplicado de la lista combinada.
Ordene la lista combinada en orden ascendente.
Imprima la lista ordenada.
'''

lista1 = [5, 3, 8, 6, 3]             
lista2 = [7, 2, 5, 9, 8]    

# Combinar las dos listas
lista_combinada = lista1 + lista2

# Eliminar duplicados
lista_combinada = list(set(lista_combinada))

# Ordenar la lista combinada en orden ascendente
lista_combinada.sort()

# Imprimir la lista ordenada
print(lista_combinada)