'''
Escribir un programa que combine dos listas en una y elimine los elementos comunes entre ellas.
Comience pegando estas dos listas en un script de Python vacío:

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

Su programa debería:
Fusionar dos listas en una sola lista.
Eliminar los elementos comunes/duplicados
Imprima la lista actualizada.
'''

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

# Combinar las dos listas
lista_combinada = lista1 + lista2

# Eliminar duplicados
lista_combinada = list(set(lista_combinada))

# Imprimir la lista actualizada
print(lista_combinada)
