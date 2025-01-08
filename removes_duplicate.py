'''
Escriba un programa que elimine elementos duplicados de una lista manteniendo el orden original. 
El programa debería devolver una nueva lista con sólo elementos únicos. Puede colocar la siguiente 
lista en su secuencia de comandos y luego agregar el código que elimina duplicados e imprime la 
nueva lista.

números = [3, 1, 2, 3, 4, 1, 5, 2]
Proporcionamos dos soluciones diferentes a este problema detrás del botón "Mostrar código" y comparamos las dos para discutir cuál es el mejor código.

El programa debería imprimir el texto "Lista sin duplicados:" seguido de la lista limpia.
'''

números = [3, 1, 2, 3, 4, 1, 5, 2]

nueva_lista = []
for número in números:
    if número not in nueva_lista:
        nueva_lista.append(número)

print("Lista sin duplicados:", nueva_lista)
