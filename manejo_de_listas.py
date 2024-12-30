'''
Crea un script de Python y pega la lista.

lista_de_comestibles = ["manzanas", "pan", "leche", "huevos", "bananas"]

-Agrega la cadena "frijoles" a la lista.
-Elimina el elemento "pan" de la lista.
-Ordena la lista alfabéticamente.
-Muestra la lista de compras actualizada.

'''

lista_de_comestibles = ["manzanas", "pan", "leche", "huevos", "bananas"]
lista_de_comestibles.append("frijoles")
lista_de_comestibles.remove("pan")
lista_de_comestibles.sort()
print(lista_de_comestibles)